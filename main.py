# main.py

import importlib
from config import SOURCES
from database import init_db_client, save_jobs # Import our new database functions

def run_engine():
    """
    The main engine. It now connects to the DB, loops through sources,
    scrapes jobs, and saves them to the database.
    """
    print("🚀 Starting JobScout AI Engine...")
    
    # Initialize the database client at the start
    db_client = init_db_client()
    if not db_client:
        print("Engine stopped due to database connection failure.")
        return

    for source in SOURCES:
        source_name = source["name"]
        source_type = source["type"]
        
        print(f"\n🔎 Processing Source: '{source_name}' (Type: {source_type})")
        
        try:
            scraper_module = importlib.import_module(f"scrapers.{source_type}_scraper")
            
            jobs = scraper_module.scrape(source)
            
            if not jobs:
                print("  -> No jobs found for this source.")
                continue

            print(f"  -> Found {len(jobs)} jobs.")
            
            # --- NEW STEP: SAVE THE JOBS TO THE DATABASE ---
            save_jobs(db_client, jobs)

        except ImportError:
            print(f"  [ERROR] Could not find a scraper for type '{source_type}'. Please check 'scrapers' folder.")
        except Exception as e:
            print(f"  [ERROR] An unexpected error occurred: {e}")
            
    print("\n✅ Engine run complete.")


if __name__ == "__main__":
    run_engine()