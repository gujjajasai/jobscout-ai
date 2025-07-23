# app.py

import streamlit as st
import pandas as pd
from database import init_db_client # We reuse our database connection function

# --- Page Configuration ---
st.set_page_config(
    page_title="JobScout AI",
    page_icon="🤖",
    layout="wide"
)

# --- Caching ---
# This is a key Streamlit feature. It "caches" the result of this function.
# This means the database is only queried once every 10 minutes, making
# the app feel incredibly fast and responsive for users.
@st.cache_data(ttl=600)
def load_data():
    """Connects to the database and fetches all jobs."""
    db_client = init_db_client()
    if not db_client:
        st.error("Could not connect to the database.")
        return pd.DataFrame() # Return empty dataframe on failure
    
    try:
        response = db_client.table('jobs').select('*').order('published_date', desc=True).execute()
        # Convert the list of dictionaries from the API response into a Pandas DataFrame
        df = pd.DataFrame(response.data)
        return df
    except Exception as e:
        st.error(f"An error occurred while fetching data: {e}")
        return pd.DataFrame()

# --- Main Application Logic ---
st.title("🤖 JobScout AI")
st.write("Your personal, automated job aggregator. All jobs, one place.")

# Load the data from the database
main_df = load_data()

if main_df.empty:
    st.warning("No data found. The database might be empty or the connection failed.")
    st.stop() # Stop the script if there's no data

# --- Sidebar for Filters ---
st.sidebar.header("Filter Jobs")

# Text search filter
search_query = st.sidebar.text_input("Search by Title", "")

# Multi-select filter for job sources
all_sources = sorted(main_df['source'].unique())
selected_sources = st.sidebar.multiselect("Filter by Source", options=all_sources, default=all_sources)

# --- Filtering Logic ---
# Start with the full dataframe and apply filters sequentially
filtered_df = main_df

if search_query:
    # Use .str.contains() for a case-insensitive search
    filtered_df = filtered_df[filtered_df['title'].str.contains(search_query, case=False, na=False)]

if selected_sources:
    filtered_df = filtered_df[filtered_df['source'].isin(selected_sources)]

# --- Display Results ---
st.header("Aggregated Job Listings")

# Display a metric showing the number of jobs found after filtering
st.metric(label="Total Jobs Found", value=len(filtered_df))

# Display the filtered jobs in a clean table.
# We rename columns for better readability and hide the index.
st.dataframe(
    filtered_df,
    column_config={
        "title": "Job Title",
        "link": st.column_config.LinkColumn("Link", display_text="Apply ↗"),
        "published_date": "Published On",
        "source": "Source"
    },
    hide_index=True,
    use_container_width=True
)