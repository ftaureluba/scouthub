
import os
import pandas as pd
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class DataService:
    def __init__(self):
        url: str = os.environ.get("SUPABASE_URL", "")
        key: str = os.environ.get("SUPABASE_KEY", "")
        if not url or not key:
            raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in environment variables")
        print(f"Connecting to Supabase at: {url}")
        self.supabase: Client = create_client(url, key)

    def get_player_id(self, player_name: str):
        """
        Fetches the ID of a player by their name from the players table.
        """
        try:
            response = self.supabase.table('players').select("id").eq("name", player_name).single().execute()
            if response.data:
                return response.data['id']
            return None
        except Exception as e:
            print(f"Error fetching player ID for {player_name}: {e}")
            return None

    def upsert_players(self, df: pd.DataFrame, mapping: dict):
        """
        Upserts player data into players table.
        """
        print(f"Upserting {len(df)} players...")
        
        # Deduplicate based on unique key 'name' (mapped from 'Player') before upserting
        # The mapping has 'Player' -> 'name'. We scan 'Player' in DF.
        df_unique = df.drop_duplicates(subset=['Player'])
        print(f"Reduced to {len(df_unique)} unique players.")

        records = []
        for _, row in df_unique.iterrows():
            record = {}
            for csv_col, db_col in mapping.items():
                if csv_col in row:
                    val = row[csv_col]
                    # Handle NaN/None
                    if pd.isna(val) or val == "":
                        val = None
                    record[db_col] = val
            
            # Clean up numeric fields that might be strings/floats
            # This is a basic cleanup, might need more robust typing based on model
            records.append(record)
        
        try:
            # Upsert in chunks to avoid payload limits if necessary, but starting simple
            # unique column is 'name'
            response = self.supabase.table('players').upsert(records, on_conflict='name').execute()
            print("Players upserted successfully.")
            return response
        except Exception as e:
            print(f"Error upserting players: {e}")
            return None

    def upsert_stats(self, table_name: str, df: pd.DataFrame, mapping: dict):
        """
        Upserts related stats (Shooting, Passing, etc.) linked to JugadorModel.
        """
        print(f"Upserting stats to {table_name}...")
        records = []
        
        # We need to map player names to IDs
        # To make this efficient, let's fetch all players needed or just query one by one?
        # Querying one by one is slow. Fetching all players might be heavy if db is huge.
        # But for a scraper run, we probably have a list of players in the DF.
        
        player_names = df['Player'].unique().tolist()
        # Fetch IDs for these players
        # Supabase 'in' filter
        player_map = {}
        
        # Fetch in chunks of 1000 to be safe
        chunk_size = 1000
        for i in range(0, len(player_names), chunk_size):
            chunk = player_names[i:i+chunk_size]
            try:
                response = self.supabase.table('players').select("id, name").in_("name", chunk).execute()
                for item in response.data:
                    player_map[item['name']] = item['id']
            except Exception as e:
                print(f"Error fetching player IDs: {e}")

        success_count = 0
        for _, row in df.iterrows():
            player_name = row.get('Player')
            if not player_name or player_name not in player_map:
                # print(f"Skipping stats for unknown player: {player_name}")
                continue
            
            player_id = player_map[player_name]
            
            record = {'player_id': player_id} # generic Foreign Key field name? Django default is fieldname_id
            # In Django OneToOneField(JugadorModel), the db column is usually player_id
            
            for csv_col, db_col in mapping.items():
                if csv_col in row:
                    val = row[csv_col]
                    if pd.isna(val) or val == "":
                        val = None
                    record[db_col] = val
            
            records.append(record)

        if not records:
             print("No records to insert.")
             return
        
        # Deduplicate records by 'player_id' to avoid "ON CONFLICT DO UPDATE command cannot affect row a second time"
        # We keep the first occurrence (or last? usually first in DF is fine or arbitrary if scraping single season)
        unique_records = {}
        for r in records:
            if r['player_id'] not in unique_records:
                unique_records[r['player_id']] = r
        
        records = list(unique_records.values())

        # Batch Upsert Logic
        # 1. Get all player_ids from current batch
        batch_player_ids = [r['player_id'] for r in records]
        
        # 2. Fetch existing rows for these players from the target table
        # We need 'id' (PK) to perform updates, and 'player_id' to match
        existing_map = {}
        try:
            # Chunking the fetch if too many IDs (Supabase URL length limits)
            # Reduced to 150 to avoid 400 Bad Request (JSON error/URL too long)
            fetch_chunk_size = 150
            for i in range(0, len(batch_player_ids), fetch_chunk_size):
                chunk_ids = batch_player_ids[i:i+fetch_chunk_size]
                response = self.supabase.table(table_name).select("id, player_id").in_("player_id", chunk_ids).execute()
                for row in response.data:
                    existing_map[row['player_id']] = row['id']
        except Exception as e:
            print(f"Error fetching existing records from {table_name}: {e}")
            # Identify what to do if fetch fails? fallback to insert might cause dupes if no constraints.
            # But let's proceed trying to safe insert. 
        
        # 3. Separate into Update and Insert lists
        to_update = []
        to_insert = []
        
        for record in records:
            p_id = record['player_id']
            if p_id in existing_map:
                # Append 'id' to record so upsert knows which row to update
                record['id'] = existing_map[p_id]
                to_update.append(record)
            else:
                to_insert.append(record)
        
        # 4. Execute Batch Operations
        print(f"Batch processing {table_name}: {len(to_update)} updates, {len(to_insert)} inserts.")
        
        try:
            if to_insert:
                # Insert new records
                # Supabase batch insert
                self.supabase.table(table_name).insert(to_insert).execute()
            
            if to_update:
                # Update existing records
                # Upsert works well if PK is provided. 
                self.supabase.table(table_name).upsert(to_update).execute()
                
            print(f"Finished processing {table_name}.")
            
        except Exception as e:
            print(f"Error during batch operation on {table_name}: {e}")
