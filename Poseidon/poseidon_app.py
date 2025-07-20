import streamlit as st

st.title("Poseidon - Trade Intelligence")

question = st.text_input("Ask a trade-related question:")

if st.button("Submit"):
    if question.strip():
        st.write(f"**Answer:** (Trade Insight) In response to: '{question}', global trade patterns are often influenced by tariffs, supply chain dynamics, and bilateral agreements.")
    else:
        st.warning("Please enter a question.")
