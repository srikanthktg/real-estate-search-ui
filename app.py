import streamlit as st
from gpt_suggestions import get_autocomplete_suggestions
from data import search_results

st.set_page_config(page_title="🏠 Smart Real Estate Search", layout="centered")
st.title("🏠 Real Estate Smart Search")

user_input = st.text_input("🔍 Start typing your property search...")

if user_input:
    with st.spinner("Getting suggestions..."):
        suggestions = get_autocomplete_suggestions(user_input)
        suggestions = [s.strip("•- ") for s in suggestions if s.strip()]

    st.subheader("💡 GPT Autocomplete Suggestions")
    for s in suggestions:
        st.markdown(f"➡️ **{s}**")

    st.subheader("📊 Sample Results")
    results = search_results(user_input)
    for r in results:
        st.write("🔹", r)
