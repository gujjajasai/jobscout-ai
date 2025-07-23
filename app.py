# app.py

import streamlit as st
import pandas as pd
from database import init_db_client
from datetime import timedelta

# --- Page Configuration: Must be the first Streamlit command ---
st.set_page_config(
    page_title="JobScout Pro",
    page_icon="🧑‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Caching: A critical performance feature ---
@st.cache_data(ttl=600)
def load_data():
    """Connects to the database, fetches all jobs, and cleans the data."""
    db_client = init_db_client()
    if not db_client:
        return pd.DataFrame() # Return empty on failure
    
    try:
        response = db_client.table('jobs').select('*').order('created_at', desc=True).limit(5000).execute()
        df = pd.DataFrame(response.data)
        
        # --- Data Cleaning and Standardization ---
        df['published_date'] = pd.to_datetime(df['published_date'], errors='coerce', utc=True)
        df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce', utc=True)
        # Fill missing values and strip whitespace from text fields for reliable filtering
        for col in ['job_role', 'experience_level', 'location', 'company', 'description', 'title']:
            df[col] = df[col].fillna('Not Specified').str.strip()
        return df
    except Exception as e:
        print(f"Data loading error: {e}")
        return pd.DataFrame()

# --- Initialize Session State for Pagination ---
if 'page' not in st.session_state:
    st.session_state.page = 0

# ====================================================================
# --- Load Data First (Fixes the NameError bug) ---
# ====================================================================
# Use an animated spinner for a better loading experience
with st.spinner("Fetching the latest jobs from the database..."):
    main_df = load_data()

# ====================================================================
# --- Sidebar Filters ---
# ====================================================================
with st.sidebar:
    st.title("🧑‍💻 JobScout Pro")
    st.write("Your intelligent job aggregator.")
    st.divider()

    st.header("🔎 Advanced Filters")
    
    if main_df.empty:
        st.warning("No data to filter.")
    else:
        # These filters can now safely use 'main_df' to get their options
        role_options = ["All Roles"] + sorted(main_df['job_role'].unique())
        selected_role = st.selectbox("**Job Role**", options=role_options)

        exp_options = ["All Experience Levels"] + sorted(main_df['experience_level'].unique())
        selected_exp = st.selectbox("**Experience Level**", options=exp_options)

        location_query = st.text_input("**Location**", placeholder="e.g., Remote, London, IN")
        
        latest_options = ["All Time", "Today", "This Week", "This Month"]
        selected_latest = st.selectbox("**Freshness**", options=latest_options)

# ====================================================================
# --- Main Content Area ---
# ====================================================================
st.header("Live Job Opportunities")

if main_df.empty:
    st.error("Could not load job data. Please check the backend or try again later.")
    st.stop()

# --- Filtering Logic ---
# This corrected logic ensures all filters are chained together correctly.
filtered_df = main_df.copy() # Start with a copy of the full dataframe

if selected_role != "All Roles":
    filtered_df = filtered_df[filtered_df['job_role'] == selected_role]

if selected_exp != "All Experience Levels":
    filtered_df = filtered_df[filtered_df['experience_level'] == selected_exp]

if location_query:
    filtered_df = filtered_df[filtered_df['location'].str.contains(location_query, case=False)]

if selected_latest != "All Time":
    now = pd.Timestamp.now(tz='UTC')
    delta_map = {"Today": 1, "This Week": 7, "This Month": 30}
    time_delta = timedelta(days=delta_map[selected_latest])
    filtered_df = filtered_df[filtered_df['created_at'] >= (now - time_delta)]

# --- Pagination Logic ---
ITEMS_PER_PAGE = 10
start_idx = st.session_state.page * ITEMS_PER_PAGE
end_idx = start_idx + ITEMS_PER_PAGE
page_df = filtered_df.iloc[start_idx:end_idx]

st.write(f"Showing **{len(page_df)}** of **{len(filtered_df)}** matching jobs.")
st.divider()

# --- Professional Card-Based Layout ---
if page_df.empty:
    st.warning("No jobs match your current filter criteria. Try broadening your search!")
else:
    for index, row in page_df.iterrows():
        with st.container(border=True):
            col1, col2 = st.columns([5, 1]) # Make the first column 5x wider
            with col1:
                st.markdown(f"#### {row['title']}")
                st.markdown(f"**🏢 Company:** {row.get('company', 'N/A')}")
            with col2:
                st.link_button("Apply Now ↗", row['link'], use_container_width=True)
            
            st.divider()
            
            tag_cols = st.columns(3)
            with tag_cols[0]:
                st.markdown(f"**📍 Location:** `{row.get('location', 'N/A')}`")
            with tag_cols[1]:
                st.markdown(f"**📈 Experience:** `{row.get('experience_level', 'N/A')}`")
            with tag_cols[2]:
                # Format the date nicely, checking if it exists first
                published_str = row.get('published_date').strftime('%d %b, %Y') if pd.notna(row.get('published_date')) else 'N/A'
                st.markdown(f"**🗓️ Published:** `{published_str}`")
            
            with st.expander("Show Job Description"):
                st.markdown(row.get('description', 'No description available.'), unsafe_allow_html=True)

# --- Pagination Buttons ---
st.divider()
page_cols = st.columns([1, 1, 1])
def prev_page(): st.session_state.page -= 1
def next_page(): st.session_state.page += 1
with page_cols[0]:
    st.button("⬅️ Previous Page", on_click=prev_page, disabled=(st.session_state.page == 0), use_container_width=True)
with page_cols[2]:
    st.button("Next Page ➡️", on_click=next_page, disabled=(end_idx >= len(filtered_df)), use_container_width=True)
