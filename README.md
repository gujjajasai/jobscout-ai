# 🧑‍💻 JobScout AI - A Global Job Aggregator

[![CI/CD Scraper Workflow](https://github.com/gujjajasai/jobscout-ai/actions/workflows/scraper_workflow.yml/badge.svg)](https://github.com/gujjajasai/jobscout-ai/actions/workflows/scraper_workflow.yml)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

JobScout AI is a fully autonomous, full-stack data application designed to solve the tedious problem of job hunting across multiple platforms. It automatically scrapes, classifies, and displays job postings from dozens of global sources in a clean, professional, and filterable user interface.

---

## 🚀 Live Demo

**Experience the live application here:**
**https://jobscout-ai-jnvpnrenkcxquqidamhmhl.streamlit.app/**

*(Note: The database is populated by an automated scraper that runs periodically. If the app is empty, the scraper is likely in the middle of a run.)*

## ✨ Key Features

*   **🤖 Automated Data Collection:** A GitHub Actions workflow runs on a schedule, autonomously scraping new job postings 24/7 without any manual intervention.
*   **🌐 Multi-Modal Scraping Engine:** The backend is architected to handle multiple data sources, using a robust engine that can process both structured **RSS feeds** (`feedparser`, `httpx`) and navigate complex, JavaScript-driven websites using **headless browser automation** (`Playwright`).
*   **🧠 Intelligent Job Classification:** An NLP utility (`utils.py`) automatically classifies each job by **Job Role** (e.g., Engineering, Data Science) and **Experience Level** (e.g., Senior, Junior) based on keywords in the title.
*   **🗃️ Centralized & Robust Database:** All collected data is stored in a professional-grade **Supabase (Postgres)** database, with logic to prevent duplicate entries.
*   **💻 Professional User Interface:** A clean, modern, and fully interactive frontend built with **Streamlit**, featuring a card-based layout, pagination, and advanced, functional filters for Job Role, Experience, and Location.

## 🛠️ Tech Stack

| Category          | Technologies                                      |
| ----------------- | ------------------------------------------------- |
| **Backend**       | Python, httpx, feedparser, Playwright, BeautifulSoup4 |
| **Frontend**      | Streamlit, Pandas                                 |
| **Database**      | Supabase (PostgreSQL)                             |
| **Automation/CI/CD** | GitHub Actions                                    |
| **Environment**   | python-dotenv, venv                               |

## 🏛️ Architecture

This project is a complete, full-stack application with a clear separation between the backend data pipeline and the frontend user interface.

```
+--------------------------+      +-----------------------------+      +-------------------------+
| GitHub Actions (Scheduler) | ---> | Scraper Engine (main.py)    | ---> | Supabase (Postgres) DB  |
| (Runs every hour)        |      | (RSS & Browser Scrapers)      |      | (Stores & Cleans Data)  |
+--------------------------+      +-----------------------------+      +-------------------------+
                                                                                  |
                                                                                  | (Reads Data)
                                                                                  |
                                                                         +---------------------+
                                                                         | Streamlit Cloud UI  |
                                                                         | (app.py)            |
                                                                         +---------------------+
```

## ⚙️ Local Setup and Installation

To run this project on your local machine, follow these steps:

**1. Clone the Repository:**
```bash
git clone https://github.com/gujjajasai/jobscout-ai.git
cd jobscout-ai
```

**2. Create and Activate a Virtual Environment:**
```bash
# Create the environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (macOS/Linux)
source venv/bin/activate
```

**3. Install Dependencies:**
```bash
pip install -r requirements.txt
```

**4. Install Browser Engines for Playwright:**
(This is required for the browser automation scraper)
```bash
playwright install
```

**5. Configure Environment Variables:**
*   Create a file named `.env` in the root of the project.
*   Add your Supabase credentials to this file:
    ```
    SUPABASE_URL="YOUR_SUPABASE_PROJECT_URL"
    SUPABASE_KEY="YOUR_SUPABASE_ANON_KEY"
    ```

## ▶️ How to Run

**1. Run the Backend Scraper (to populate the database):**
```bash
python main.py
```
*Wait for the engine to complete its run.*

**2. Run the Frontend Application:**
```bash
streamlit run app.py
```
*Your browser should automatically open to `http://localhost:8501`.*

## 📈 Future Roadmap

*   **Expand Scraper Modules:** Build new, dedicated scrapers for expert-level targets like LinkedIn and Naukri that require handling logins.
*   **Email & Telegram Notifications:** Add a notification module to the backend to send daily digests of new, relevant jobs.
*   **User Accounts & Saved Jobs:** Implement user authentication to allow users to save jobs to a personal list.
*   **Data Visualizations:** Add a "Dashboard" page to the UI with charts showing job trends, top companies, and role distributions.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.