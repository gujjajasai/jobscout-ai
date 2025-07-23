# main.py

import importlib
from config import SOURCES
from database import init_db_client, save_jobs

def run_engine():
    """
    This is the main engine. It connects to the DB, loops through the
    massive list of sources in config.py, dynamically loads the correct
    scraper tool for each source, runs it, and saves the results.
    """
    print("🚀 Starting JobScout AI Engine...")
    
    # Initialize the database client at the very start of the run.
    db_client = init_db_client()
    if not db_client:
        print("Engine stopped due to database connection failure.")
        return

    # Loop through every source defined in our config file.
    for source in SOURCES:
        source_name = source["name"]
        source_type = source["type"]
        
        print(f"\n🔎 Processing Source: '{source_name}' (Type: {source_type})")
        
        try:
            # This is the core of our modular design. It dynamically finds and
            # loads the correct scraper module (e.g., "scrapers.rss_scraper"
            # or "scrapers.browser_scraper") based on the 'type' field.
            scraper_module = importlib.import_module(f"scrapers.{source_type}_scraper")
            
            # Now, we call the 'scrape' function that we know exists in that module.
            jobs = scraper_module.scrape(source)
            
            if not jobs:
                print("  -> No jobs found for this source.")
                continue

            print(f"  -> Found {len(jobs)} jobs.")
            
            # Pass the collected jobs and the database client to our save function.
            save_jobs(db_client, jobs)

        except ImportError:
            print(f"  [ERROR] Could not find a scraper for type '{source_type}'. Please check your 'scrapers' folder.")
        except Exception as e:
            # This is a general catch-all to ensure one failed source doesn't crash the entire engine.
            print(f"  [ERROR] An unexpected error occurred while processing {source_name}: {e}")
            
    print("\n✅ Engine run complete.")


# This ensures the code only runs when you execute "python main.py" from the terminal.
if __name__ == "__main__":
    run_engine()