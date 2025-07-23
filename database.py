# database.py

import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

def init_db_client():
    """Initializes and returns the Supabase client."""
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    
    if not url or not key:
        print("[ERROR] Supabase URL or Key not found in .env file.")
        return None
        
    try:
        supabase_client = create_client(url, key)
        print("✅ Database client initialized successfully.")
        return supabase_client
    except Exception as e:
        print(f"[ERROR] Failed to initialize database client: {e}")
        return None

def save_jobs(client: Client, jobs: list):
    """
    Saves a list of job dictionaries to the Supabase 'jobs' table,
    now including company and description details.
    """
    if not client or not jobs:
        return

    print(f"  -> Attempting to save {len(jobs)} jobs to the database...")
    
    records_to_insert = []
    for job in jobs:
        # --- UPGRADED RECORD DICTIONARY ---
        # This now includes all the new fields to match our upgraded database table.
        # We use .get() to safely handle cases where a field might be missing.
        record = {
            "title": job.get("title"),
            "link": job.get("link"),
            "published_date": job.get("published_date"),
            "source": job.get("source"),
            "company": job.get("company"),
            "description": job.get("description"),
            "job_role": job.get("job_role"), # New field
            "experience_level": job.get("experience_level") # New field
            # The 'location' field will mostly be NULL for RSS feeds, which is fine.
        }
        # We only process jobs that have a valid link.
        if record["link"]:
            records_to_insert.append(record)

    # If there are no valid records to insert, we can stop here.
    if not records_to_insert:
        print("  -> No valid jobs with links to save.")
        return

    try:
        # The 'upsert' command is the core of our logic. It will INSERT new jobs.
        # If a job with the same 'link' (our unique column) already exists,
        # the database will simply ignore it, preventing duplicates.
        response = client.table('jobs').upsert(records_to_insert, on_conflict='link').execute()
        
        if response.data:
            num_saved = len(response.data)
            num_duplicates = len(records_to_insert) - num_saved
            print(f"  -> 🎉 Success! Saved {num_saved} new jobs. Skipped {num_duplicates} duplicates.")
        else:
            print("  -> No new jobs to save. All entries were likely duplicates.")
            
    except Exception as e:
        print(f"  [ERROR] Could not save jobs to database: {e}")