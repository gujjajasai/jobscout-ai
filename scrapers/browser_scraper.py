# scrapers/browser_scraper.py

from playwright.sync_api import sync_playwright
from utils import classify_role, classify_experience
from bs4 import BeautifulSoup # We might use this for cleaning descriptions

def scrape(source):
    """
    Scrapes jobs using a headless browser, with more robust and defensive logic
    to handle missing elements on individual job cards.
    """
    
    jobs_list = []
    
    print(f"  -> [Browser] Launching browser to scrape {source['name']}...")
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            page.goto(source["url"], timeout=60000) # 60-second timeout to load the page
            
            # Wait for the main container of job listings to appear
            page.wait_for_selector(source["selectors"]["job_card"], timeout=30000)
            
            job_cards = page.locator(source["selectors"]["job_card"]).all()
            print(f"  -> Found {len(job_cards)} potential job cards on the page.")

            # Limit to the first 20 cards to be respectful to the site and improve speed
            for card in job_cards[:20]:
                try:
                    # --- UPGRADED: Defensive data extraction ---
                    # For each piece of data, we check if the element exists before trying to get its text.
                    # This prevents one bad card from stopping the whole scrape.
                    
                    title_element = card.locator(source["selectors"]["title"])
                    link_element = card.locator(source["selectors"]["link"])
                    
                    # Core data must exist, otherwise we skip the card.
                    if not title_element.count() or not link_element.count():
                        continue

                    title = title_element.inner_text().strip()
                    link = link_element.get_attribute('href')
                    
                    if link and not link.startswith('http'):
                        link = source.get('base_url', '') + link

                    # Safely get optional details with default values
                    company_selector = source["selectors"].get("company")
                    company = card.locator(company_selector).inner_text().strip() if company_selector and card.locator(company_selector).count() > 0 else "Not Specified"

                    desc_selector = source["selectors"].get("description")
                    description = card.locator(desc_selector).inner_text().strip() if desc_selector and card.locator(desc_selector).count() > 0 else "No description"
                    
                    loc_selector = source["selectors"].get("location")
                    location = card.locator(loc_selector).inner_text().strip() if loc_selector and card.locator(loc_selector).count() > 0 else "Not Specified"

                    job = {
                        "title": title,
                        "link": link,
                        "source": source["name"],
                        "company": company,
                        "description": description,
                        "location": location,
                        # Use our AI utility to classify the role and experience
                        "job_role": classify_role(title),
                        "experience_level": classify_experience(title)
                    }
                    jobs_list.append(job)

                except Exception as e:
                    print(f"    [Warning] Could not parse a job card for {source['name']}: {e}")
                    continue

            browser.close()
            
    except Exception as e:
        print(f"  [ERROR] An error occurred during browser automation for '{source['name']}': {e}")
        return []

    return jobs_list