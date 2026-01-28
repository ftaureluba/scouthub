
import sys
import os
# Add parent directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from db import supabase

def test_insert():
    print("Testing Supabase Connection...")
    try:
        data = {
            "name": "Test Player",
            "team": "Test FC",
            "nation": "AR",
            "goals": 10
        }
        response = supabase.table('players').upsert(data).execute()
        print("Success! Inserted:", response.data)
    except Exception as e:
        print("Error connecting to Supabase:", e)

if __name__ == "__main__":
    test_insert()
