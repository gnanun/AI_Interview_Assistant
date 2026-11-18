pip install -q groq
from groq import Groq
import streamlit as st
st.set_page_config(page_title="Gnanesh N", page_icon="🥰",layout="centered")
st.title("AI Interview Assistance")
st.caption("Practice and Prepare for your placements here")
try:
  client=Groq(api_key=st.secrets["GROQ_API_KEY"])
except: (keyError, FileNotFound):
  st.error("API key is missing. addit in advanced settings")
  st.stop()
