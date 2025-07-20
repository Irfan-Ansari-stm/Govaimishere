import streamlit as st

st.title("Triton - Open Source Intelligence")

question = st.text_input("Ask something based on open data:")

if st.button("Submit"):
    if question.strip():
        st.write(f"**Answer:** (OSINT Insight) Regarding: '{question}', publicly available sources like news, social media, and government databases provide useful intelligence.")
    else:
        st.warning("Please enter a question.")
