
import os
import sys
from services.fbref import Fbref
# Add the current directory to sys.path to make imports work easiest
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


if __name__ == "__main__":
    print("Starting Scraper...")

    fbref = Fbref()

    data = fbref.get_all_player_season_stats("Copa de la Liga", "2024")
    print("Scraping Finished.")
    print(data)
    