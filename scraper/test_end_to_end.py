
import asyncio
import sys
import os
from services.fbref import Fbref
from services.data_service import DataService

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

async def run_test():
    print("--- Starting End-to-End Test ---")
    
    # Initialize Scraper
    fbref = Fbref()
    
    # LIMIT the stats to just 'stats' (standard) and 'shooting' for speed
    fbref.possible_stats = ['stats', 'shooting']
    
    # Run Scrape for a specific league/season
    # choosing a league that likely has data. "Copa de la Liga" "2024" was in main.py
    print("Scraping 'Copa de la Liga' 2024 (Limited to standard & shooting stats)...")
    
    # We need to run the internal async method directly or via the wrapper
    # The wrapper is synchronous, so we can't await it here easily if we are already async?
    # Actually, main.py calls synchronous wrapper. Let's use the wrapper but we are in async def.
    # To avoid nested event loops if we used asyncio.run inside wrapper:
    # We should call the async method directly.
    
    try:
        data, gk_data = await fbref._get_all_player_season_stats_async("Copa de la Liga", "2024")
        print("Scraping completed.")
        
        # Verify Player Data in Supabase
        print("Verifying data in Supabase...")
        ds = DataService()
        
        # Check for a known player likely to be there, or just count rows
        # Let's count rows in 'players'
        response = ds.supabase.table('players').select("*", count='exact').limit(1).execute()
        count = response.count
        print(f"Total rows in 'players' table: {count}")
        
        if count > 0:
            print("SUCCESS: Players table has data.")
        else:
            print("FAILURE: Players table is empty.")

        # Check 'stats_shooting'
        response_sh = ds.supabase.table('stats_shooting').select("*", count='exact').limit(1).execute()
        count_sh = response_sh.count
        print(f"Total rows in 'stats_shooting' table: {count_sh}")
        
        if count_sh > 0:
            print("SUCCESS: Shooting stats table has data.")
        else:
            print("FAILURE: Shooting stats table is empty.")
            
    except Exception as e:
        print(f"Test Failed with error: {e}")

if __name__ == "__main__":
    asyncio.run(run_test())
