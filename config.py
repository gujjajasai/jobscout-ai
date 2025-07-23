# config.py

# This is the master list of high-yield, global RSS feeds, curated from
# the provided list to maximize job collection on a global scale.

SOURCES = [
    # --- Major Remote Job Aggregators ---
    { "name": "We Work Remotely - All Jobs", "url": "https://weworkremotely.com/remote-jobs.rss", "type": "rss" },
    { "name": "RemoteOK", "url": "https://remoteok.com/remote-jobs.rss", "type": "rss" },
    { "name": "Remotive", "url": "https://remotive.com/api/remote-jobs/feed", "type": "rss" },
    { "name": "Jobspresso", "url": "https://jobspresso.co/feed/", "type": "rss" },
    { "name": "Himalayas", "url": "https://himalayas.app/jobs/rss", "type": "rss" },
    { "name": "Jobicy", "url": "https://jobicy.com/feed/job_feed", "type": "rss" },
    { "name": "FlexJobs", "url": "https://www.flexjobs.com/rss-feeds.html", "type": "rss" }, # Note: This links to a page of feeds, direct scraping might be complex.
    { "name": "SkipTheDrive", "url": "https://www.skipthedrive.com/feed/", "type": "rss" },
    { "name": "EuropeRemotely", "url": "https://europeremotely.com/feed/", "type": "rss" },

    # --- WWR Category-Specific Feeds ---
    { "name": "WWR - Customer Support", "url": "https://weworkremotely.com/categories/remote-customer-support-jobs.rss", "type": "rss" },
    { "name": "WWR - Product", "url": "https://weworkremotely.com/categories/remote-product-jobs.rss", "type": "rss" },
    { "name": "WWR - Full-Stack Programming", "url": "https://weworkremotely.com/categories/remote-full-stack-programming-jobs.rss", "type": "rss" },
    { "name": "WWR - Back-End Programming", "url": "https://weworkremotely.com/categories/remote-back-end-programming-jobs.rss", "type": "rss" },
    { "name": "WWR - Front-End Programming", "url": "https://weworkremotely.com/categories/remote-front-end-programming-jobs.rss", "type": "rss" },
    { "name": "WWR - All Programming", "url": "https://weworkremotely.com/categories/remote-programming-jobs.rss", "type": "rss" },
    { "name": "WWR - Sales & Marketing", "url": "https://weworkremotely.com/categories/remote-sales-and-marketing-jobs.rss", "type": "rss" },
    { "name": "WWR - Management & Finance", "url": "https://weworkremotely.com/categories/remote-management-and-finance-jobs.rss", "type": "rss" },
    { "name": "WWR - Design", "url": "https://weworkremotely.com/categories/remote-design-jobs.rss", "type": "rss" },
    { "name": "WWR - DevOps & SysAdmin", "url": "https://weworkremotely.com/categories/remote-devops-sysadmin-jobs.rss", "type": "rss" },
    { "name": "WWR - All Other", "url": "https://weworkremotely.com/categories/all-other-remote-jobs.rss", "type": "rss" },

    # --- Tech & Language-Specific Boards ---
    { "name": "Stack Overflow", "url": "https://stackoverflow.com/jobs/feed", "type": "rss" },
    { "name": "Python.org Jobs", "url": "https://www.python.org/jobs/rss/", "type": "rss" },
    { "name": "Laravel Jobs", "url": "https://larajobs.com/feed", "type": "rss" },
    { "name": "Vue.js Jobs", "url": "https://vuejobs.com/jobs.rss", "type": "rss" },
    { "name": "Golang Cafe", "url": "https://www.golang.cafe/golang-jobs.rss", "type": "rss" },
    { "name": "Ruby Now", "url": "https://jobs.rubynow.com/rss", "type": "rss" },
    { "name": "CryptoJobsList", "url": "https://cryptojobslist.com/rss", "type": "rss" },
    { "name": "Edge Tech Recruitment", "url": "https://edgetech.ai/feed", "type": "rss" },
    
    # --- Design, Marketing & Creative Boards ---
    { "name": "Dribbble Jobs", "url": "https://dribbble.com/jobs.rss", "type": "rss" },
    { "name": "Behance Jobs", "url": "https://www.behance.net/joblist/rss", "type": "rss" },
    { "name": "Authentic Jobs", "url": "https://authenticjobs.com/feed/", "type": "rss" },
    { "name": "ProBlogger (Content)", "url": "https://problogger.com/jobs/feed/", "type": "rss" },
    { "name": "Moz Blog (Marketing)", "url": "https://moz.com/posts/rss/blog", "type": "rss" },

    # --- Startup, Academic & Niche Boards ---
    { "name": "AngelList / Wellfound", "url": "https://wellfound.com/jobs.rss", "type": "rss" },
    { "name": "jobs.ac.uk (Tech)", "url": "https://www.jobs.ac.uk/feeds/subject-areas/engineering-and-technology", "type": "rss" },
    { "name": "HigherEdJobs (Finance)", "url": "https://www.higheredjobs.com/rss/categoryFeed.cfm?catID=44", "type": "rss" },
    { "name": "HigherEdJobs (Marketing)", "url": "https://www.higheredjobs.com/search/rss.cfm?JobCat=47", "type": "rss" },

    # --- India-Specific Boards ---
    { "name": "Internshala", "url": "https://internshala.com/rss.xml", "type": "rss" },
    { "name": "Freshersworld", "url": "https://www.freshersworld.com/rss.php", "type": "rss" },

    # --- Direct Company Career Feeds ---
    { "name": "Google Careers", "url": "https://careers.google.com/jobs/results/rss/", "type": "rss" },
    { "name": "Microsoft Careers", "url": "https://careers.microsoft.com/us/en/search-results/rss", "type": "rss" },
    { "name": "GitLab Jobs", "url": "https://about.gitlab.com/jobs/feed.xml", "type": "rss" },
    { "name": "Mozilla Careers", "url": "https://careers.mozilla.org/rss/jobs/", "type": "rss" },
    { "name": "Automattic Jobs", "url": "https://automattic.com/jobs/feed/", "type": "rss" },
    { "name": "Salesforce Careers", "url": "https://www.salesforce.com/company/careers/rss/", "type": "rss" },
    # In config.py, add this to the SOURCES list:

    {
        "name": "Wellfound (formerly AngelList)",
        "url": "https://wellfound.com/jobs.rss",
        "type": "rss"
    },
    # In config.py, add this to the SOURCES list:

    {
        "name": "InternFreak",
        "url": "https://internfreak.co/internships",
        "type": "browser", # This tells the engine to use browser_scraper.py
        "base_url": "https://internfreak.co",
        "selectors": {
            "job_card": "div.if-internship-card",
            "title": "h3.if-title",
            "link": "a.if-card-btn",
            "company": "p.if-company",
            "description": "div.if-stipend" # We'll use the stipend/details section as the description
        }
    },
    # In config.py, at the end of the SOURCES list:

    # --- NEW BROWSER-BASED SCRAPER TARGET ---
    # This is an EXAMPLE. These selectors need to be found manually for a real site.
    {
        "name": "Indeed (Example: Python in Texas)",
        "url": "https://www.indeed.com/jobs?q=python&l=Texas",
        "type": "browser", # This tells the engine to use our new browser_scraper.py
        "base_url": "https://www.indeed.com",
        "selectors": {
            "job_card": "div.job_seen_beacon",
            "title": "h2.jobTitle",
            "link": "a.jcs-JobTitle",
            "company": "span.companyName",
            "description": "div.job-snippet"
        }
    },
    {
        "name": "Wellfound (formerly AngelList)",
        "url": "https://wellfound.com/jobs.rss",
        "type": "rss"
    },

    # ====================================================================
    # Tier 2: Fresher Boards from Your List (Browser Automation)
    # ====================================================================
    {
        "name": "InternFreak",
        "url": "https://internfreak.co/internships",
        "type": "browser",
        "base_url": "https://internfreak.co",
        "selectors": {
            "job_card": "div.if-internship-card",
            "title": "h3.if-title",
            "link": "a.if-card-btn",
            "company": "p.if-company",
            "description": "div.if-stipend"
        }
    },
    {
        "name": "Freshers Jobs 24",
        "url": "https://freshersjobs24.com/",
        "type": "browser",
        "base_url": "https://freshersjobs24.com",
        "selectors": {
            "job_card": "article.post-item",
            "title": "h2.post-title a",
            "link": "h2.post-title a",
            "company": ".post-meta .post-author",
            "description": ".post-excerpt"
        }
    },
    {
        "name": "FreshersVoice",
        "url": "https://www.freshersvoice.com/",
        "type": "browser",
        "base_url": "https://www.freshersvoice.com",
        "selectors": {
            "job_card": "article.jeg_post",
            "title": "h3.jeg_post_title a",
            "link": "h3.jeg_post_title a",
            "company": "div.jeg_post_meta .jeg_meta_author", # This might be unreliable
            "description": "div.jeg_post_excerpt p"
        }
    }

]