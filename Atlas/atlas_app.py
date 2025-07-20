import streamlit as st
st.title("Atlas - Geopolitical Intelligence")
question = st.text_input("Ask a geopolitical question:")
if st.button("Submit"):
    if question.strip():
        response = f"(Geopolitical Insight) Considering your question: '{question}', geopolitical stability often depends on international relations and domestic governance."
        st.write("**Answer:**", response)
    else:
        st.warning("Please enter a geopolitical question.")
