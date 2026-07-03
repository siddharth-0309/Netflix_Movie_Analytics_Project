import streamlit as st
import pandas as pd
import plotly.express as px

# Page setup
st.set_page_config(page_title="Netflix Movie Dashboard", layout="wide")

st.title("🎬 Netflix Movie Data Explorer")
st.write("This is a data analysis project showcasing insights from the Netflix movie database.")

# 1. Load the data
@st.cache_data
def load_data():
   
    df = pd.read_csv('mymoviedb.csv', encoding='latin-1', on_bad_lines='skip')
    return df

try:
    df = load_data()

    # 2. Sidebar Filters
    st.sidebar.header("Filters")
    # Handling potential missing values in Genre column
    genres = df['Genre'].dropna().unique()
    selected_genres = st.sidebar.multiselect("Select Genre:", options=genres)
    
    # Filtering logic
    filtered_df = df
    if selected_genres:
        filtered_df = df[df['Genre'].isin(selected_genres)]

    # 3. Layout (Metrics)
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Movies/Shows", len(filtered_df))
    col2.metric("Average Rating", round(filtered_df['Vote_Average'].mean(), 2))
    col3.metric("Total Votes", f"{filtered_df['Vote_Count'].sum():,}")

    # 4. Graphs (Visuals)
    st.subheader("Analysis")
    fig = px.scatter(
        filtered_df, 
        x="Release_Date", 
        y="Vote_Average", 
        color="Genre", 
        title="Movie Ratings Over Time",
        hover_data=['Title']
    )
    st.plotly_chart(fig, use_container_width=True)

    # 5. Data Preview
    st.subheader("Data Table")
    st.dataframe(filtered_df, use_container_width=True)

except Exception as e:
    st.error(f"An error occurred: {e}")
    st.info("Please ensure that 'mymoviedb.csv' is uploaded in the same repository as 'app.py'.")
