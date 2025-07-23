# scrapers/rss_scraper.py

import feedparser
import httpx # Import the new library

# This is our browser disguise
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# Define our timeout in seconds
NETWORK_TIMEOUT = 15.0

def scrape(source):
    """
    Scrapes an RSS feed by first fetching the content with a timeout,
    and then parsing it.
    """
    
    headers = {'User-Agent': USER_AGENT}
    jobs_list = []
    
    print(f"  -> Fetching content from {source['name']}...")
    try:
        # --- THIS IS THE NEW, ROBUST NETWORKING LOGIC ---
        # We use httpx to make the request with a specific timeout.
        with httpx.Client(headers=headers, timeout=NETWORK_TIMEOUT, follow_redirects=True) as client:
            response = client.get(source["url"])
            # This line will raise an error if the status is bad (like 404 or 500)
            response.raise_for_status()

        # If the request was successful, we now give the content to feedparser
        feed = feedparser.parse(response.text)

        for entry in feed.entries:
            job = {
                "title": entry.title,
                "link": entry.link,
                "published_date": entry.get('published', 'N/A'),
                "source": source["name"]
            }
            jobs_list.append(job)
            
    # --- NEW, MORE SPECIFIC ERROR HANDLING ---
    except httpx.TimeoutException:
        print(f"  [ERROR] Network timeout: The request to '{source['name']}' took too long.")
        return [] # Return an empty list
    except httpx.RequestError as e:
        print(f"  [ERROR] A network error occurred with '{source['name']}': {e}")
        return [] # Return an empty list
    except Exception as e:
        # Catch any other unexpected errors during parsing
        print(f"  [ERROR] An unexpected error occurred: {e}")
        return []

    return jobs_list