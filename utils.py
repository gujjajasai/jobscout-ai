# utils.py

# This file contains the "AI" logic to classify jobs based on their titles.
# It's a simple but powerful form of Natural Language Processing (NLP).

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

def classify_role(title):
    """Classifies the job role based on keywords in the title."""
    title_lower = title.lower()
    for role, keywords in ROLE_KEYWORDS.items():
        if any(keyword in title_lower for keyword in keywords):
            return role
    return "Other" # Default category if no keywords match

def classify_experience(title):
    """Classifies the experience level based on keywords in the title."""
    title_lower = title.lower()
    # Check in order of seniority to avoid misclassification (e.g., "Senior Lead" as "Lead")
    for level, keywords in EXPERIENCE_KEYWORDS.items():
        if any(keyword in title_lower for keyword in keywords):
            return level
    return "Not Specified" # Default if no experience level is mentioned