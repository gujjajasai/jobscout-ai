# scrapers/rss_scraper.py

import httpx
import feedparser
from utils import classify_role, classify_experience

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
NETWORK_TIMEOUT = 15.0

# --- NEW: A smarter helper function to find details ---
def extract_details(entry):
    """
    Acts like a detective to find the company name from various possible fields.
    Also cleans up the description text.
    """
    # Try to find company name in order of preference
    company = entry.get('author', 'Not Specified')
    if company == 'Not Specified' and 'dc' in entry and 'creator' in entry.dc:
        company = entry.dc.creator
    
    # Clean up the description to remove common RSS junk
    description = entry.get('summary', 'No description available.')
    if '<' in description and '>' in description:
        # A simple way to strip basic HTML tags for cleaner display
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(description, 'html.parser')
        description = soup.get_text(separator=' ', strip=True)

    return company.strip(), description

def scrape(source):
    """
    Scrapes an RSS feed, now using a helper function to extract richer data.
    """
    headers = {'User-Agent': USER_AGENT}
    jobs_list = []
    
    print(f"  -> [RSS] Fetching content from {source['name']}...")
    try:
        with httpx.Client(headers=headers, timeout=NETWORK_TIMEOUT, follow_redirects=True) as client:
            response = client.get(source["url"])
            response.raise_for_status()

        feed = feedparser.parse(response.text)

        for entry in feed.entries:
            title = entry.get('title', 'No Title')
            
            # --- UPGRADED: Use the helper function ---
            company, description = extract_details(entry)

            job = {
                "title": title,
                "link": entry.get('link'),
                "published_date": entry.get('published', None),
                "source": source["name"],
                "company": company,
                "description": description,
                # Location is rarely available in RSS feeds, will default to "Not Specified"
                "location": entry.get('location', 'Not Specified'), 
                "job_role": classify_role(title),
                "experience_level": classify_experience(title)
            }
            jobs_list.append(job)
            
    except Exception as e:
        print(f"  [ERROR] An unexpected error occurred while parsing '{source['name']}': {e}")
        return []

    return jobs_list