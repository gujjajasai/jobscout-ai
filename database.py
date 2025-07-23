# database.py

import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load the secret keys from our .env file
load_dotenv()

# --- Database Initialization ---
def init_db_client():
    """Initializes and returns the Supabase client."""
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    
    if not url or not key:
        print("[ERROR] Supabase URL or Key not found. Make sure .env file is set up correctly.")
        return None
        
    try:
        supabase_client = create_client(url, key)
        print("✅ Database client initialized successfully.")
        return supabase_client
    except Exception as e:
        print(f"[ERROR] Failed to initialize database client: {e}")
        return None

# --- Data Saving Logic ---
def save_jobs(client: Client, jobs: list):
    """Saves a list of job dictionaries to the Supabase 'jobs' table."""
    if not client or not jobs:
        return

    print(f"  -> Attempting to save {len(jobs)} jobs to the database...")
    
    # We need to make sure our job dictionary keys match the database column names exactly.
    # Let's create a list of dictionaries that are cleaned and ready for insertion.
    records_to_insert = []
    for job in jobs:
        record = {
            "title": job.get("title"),
            "link": job.get("link"),
            "published_date": job.get("published_date"),
            "source": job.get("source")
        }
        records_to_insert.append(record)

    try:
        # The 'upsert' command will INSERT new jobs. If a job with the same 'link'
        # (our unique column) already exists, it will be ignored.
        # This elegantly handles duplicates.
        response = client.table('jobs').upsert(records_to_insert, on_conflict='link').execute()
        
        # Supabase v2 returns a response with a 'data' attribute
        if response.data:
            num_saved = len(response.data)
            # We can estimate duplicates by comparing the number of jobs we sent
            # with the number of jobs that were actually inserted.
            num_duplicates = len(jobs) - num_saved
            print(f"  -> 🎉 Success! Saved {num_saved} new jobs. Skipped {num_duplicates} duplicates.")
        else:
            # This can happen if all jobs were duplicates.
            print("  -> No new jobs to save. All entries were duplicates.")

    except Exception as e:
        print(f"  [ERROR] Could not save jobs to database: {e}")