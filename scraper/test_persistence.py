
import sys
import os
import pandas as pd
import asyncio
from services.data_service import DataService
from services.mappings import STAT_TO_DB_CONFIG

# Add parent directory to path to allow imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_manual_persistence():
    service = DataService()
    
    print("--- Testing Player Upsert ---")
    # Mock 'stats' data
    player_data = {
        'Player': ['Test Player Persistence'],
        'Nation': ['AR'],
        'Pos': ['FW'],
        'Age': ['25'],
        'MP': [10],
        'Starts': [10],
        'Min': [900],
        '90s': [10.0],
        'Gls': [5],
        'Ast': [2],
        'stats_Squad': ['Test FC']
    }
    df_players = pd.DataFrame(player_data)
    
    # Get mapping for stats
    table_name_players, mapping_players = STAT_TO_DB_CONFIG['stats']
    
    response = service.upsert_players(df_players, mapping_players)
    if response:
        print("Player insert successful.")
    else:
        print("Player insert failed.")

    print("\n--- Testing Stats Upsert (Shooting) ---")
    # Mock 'shooting' data
    shooting_data = {
        'Player': ['Test Player Persistence'],
        'Gls': [5],
        'Sh': [20],
        'SoT': [10],
        'SoT%': [50.0],
        'xG': [4.5]
    }
    df_shooting = pd.DataFrame(shooting_data)
    
    table_name_shooting, mapping_shooting = STAT_TO_DB_CONFIG['shooting']
    
    service.upsert_stats(table_name_shooting, df_shooting, mapping_shooting)
    print("Test finished.")

if __name__ == "__main__":
    test_manual_persistence()
