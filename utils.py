# utils.py

# This file contains the "AI" logic to classify jobs.

ROLE_KEYWORDS = {
    "Engineering": ["engineer", "developer", "dev", "software", "backend", "frontend", "full-stack", "programmer", "code", "architect"],
    "Data Science": ["data", "scientist", "analyst", "analytics", "machine learning", "ml", "ai", "intelligence"],
    "DevOps/SysAdmin": ["devops", "sysadmin", "system administrator", "infrastructure", "cloud", "site reliability", "sre"],
    "Design/Creative": ["design", "designer", "ui", "ux", "artist", "creative", "graphic"],
    "Marketing": ["marketing", "seo", "content", "social media", "growth"],
    "Product/Management": ["product", "manager", "project", "lead", "finance", "management"],
    "Sales/Support": ["sales", "support", "customer", "business development", "bd"]
}

EXPERIENCE_KEYWORDS = {
    "Senior": ["senior", "sr.", "lead", "principal", "staff", "manager"],
    "Mid-Level": ["mid", "mid-level", "ii", "iii"],
    "Junior/Entry-Level": ["junior", "jr.", "entry", "associate", "graduate", "level i"],
    "Internship": ["intern", "internship"]
}

# --- NEW: Keywords for Location Classification ---
LOCATION_KEYWORDS = {
    "Remote": ["remote", "wfh", "work from home", "anywhere"],
    "India": ["india", "bangalore", "bengaluru", "pune", "mumbai", "hyderabad", "chennai", "delhi", "gurgaon", "noida", "in"]
}


def classify_role(title):
    title_lower = title.lower()
    for role, keywords in ROLE_KEYWORDS.items():
        if any(keyword in title_lower for keyword in keywords):
            return role
    return "Other"

def classify_experience(title):
    title_lower = title.lower()
    for level, keywords in EXPERIENCE_KEYWORDS.items():
        if any(keyword in title_lower for keyword in keywords):
            return level
    return "Not Specified"

# --- NEW: The Location Classification Function ---
def classify_location(title, description):
    """Classifies the location based on keywords in the title and description."""
    text_to_search = (title + " " + description).lower()
    
    # Prioritize "Remote" as it's the most specific
    if any(keyword in text_to_search for keyword in LOCATION_KEYWORDS["Remote"]):
        return "Remote"
        
    if any(keyword in text_to_search for keyword in LOCATION_KEYWORDS["India"]):
        return "India"
        
    return "Global"