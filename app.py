import streamlit as st
import pandas as pd
from utils.search import get_collaboration_data

st.set_page_config(page_title="Virgin Media Collaboration Finder", layout="centered")

st.title("🕵️ Virgin Media - Competitor Collaboration Finder")
st.markdown("Use this tool to find which competitors have worked with **Virgin Media**.")

# ✅ Load competitor list
try:
    competitors_df = pd.read_csv("data/competitors.csv")
    competitors = competitors_df['Company'].dropna().tolist()
except FileNotFoundError:
    st.error("❌ File not found: data/competitors.csv")
    st.stop()
except pd.errors.EmptyDataError:
    st.error("❌ The competitors.csv file is empty.")
    st.stop()

# ✅ Run search
if st.button("🔍 Run Collaboration Search"):
    with st.spinner("Searching... This may take a few moments..."):
        result_df = get_collaboration_data(competitors)
        if not result_df.empty:
            result_df.to_csv("results/virgin_collab_results.csv", index=False)
            st.success("✅ Search Completed!")
            st.dataframe(result_df)
        else:
            st.warning("⚠️ No collaboration data found. Nothing was saved.")

# ✅ Show saved results
if st.button("📂 Show Saved Results"):
    try:
        saved_df = pd.read_csv("results/virgin_collab_results.csv")
        if saved_df.empty:
            st.warning("⚠️ The saved file is empty. Try running the search again.")
        else:
            st.success("✅ Loaded saved results.")
            st.dataframe(saved_df)
    except FileNotFoundError:
        st.warning("⚠️ No saved results found. Please run the search first.")
    except pd.errors.EmptyDataError:
        st.warning("⚠️ The saved file exists but is empty or invalid.")
