import streamlit as st
from groq import Groq

st.set_page_config(page_title="Gnanesh N", page_icon="🥰",layout="centered")
st.title("AI Interview Assistance")
st.caption("Practice and Prepare for your placements here")
try:
  client=Groq(api_key=st.secrets["GROQ_API_KEY"])
except (keyError, FileNotFoundError):
  st.error("API key is missing. addit in advanced settings")
  st.stop()
role=st.selectbox("Job Title",["select","devops","AI Engineer","Data Analyst","Test engineer","other"])
if role =="other":
  st.text_input("Enter your Job Title", "XXXXXX")
model=st.selectbox("Model",["select","openai/gpt-oss-20b","openai/gpt-oss-120b","other"])
if model =="other":
  st.text_input("Enter your Job Title", "XXXXXX")
