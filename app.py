# app.py
import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set FastAPI backend URL
BACKEND_URL = "http://127.0.0.1:8000/ask"

# Streamlit UI
st.set_page_config(page_title="ProfBot", page_icon="🤖")
st.title("🤖 Agentic Prof. Assistant")
st.markdown("Ask anything from PDF + web + LangSmith-traced agent.")

# Input field
user_query = st.text_input("Enter your question:", placeholder="e.g., What is fluid mechanics?")

if st.button("Submit"):
    if user_query.strip() == "":
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = requests.post(BACKEND_URL, json={"question": user_query})

                if response.status_code == 200:
                    st.success("Agent's Response:")
                    st.write(response.json()["response"])
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")
