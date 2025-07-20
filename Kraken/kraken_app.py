import streamlit as st
st.title("Kraken - Financial Intelligence")
question = st.text_input("Ask a financial question:")
if st.button("Submit"):
    if question.strip():
        response = f"(Financial Insight) Based on your question: '{question}', a common financial strategy is to diversify investments to minimize risk."
        st.write("**Answer:**", response)
    else:
        st.warning("Please enter a financial question.")
