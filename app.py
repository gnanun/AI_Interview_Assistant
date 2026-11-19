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
model=st.selectbox("Model",["select","openai/gpt-oss-20b","openai/gpt-oss-120b"])
level=st.selectbox("Difficulty Level",["select","Advanced","Intermediate","Beginner"])
mode=st.radio("Activity",["Generate Questions","Generate Code Questions","Evaluate Answeres", "Improve the Answeres"])
if mode=="Generate Questions":
  count=st.slider("Number of Questions", 1,10,5)
elif mode=="Generate Code Questions":
  topic=st.selectbox("Topics",["AIML","C/C++", "PYTHON","JAVA","DSA","DEVOPS","SQL","MYSQL"])
  count=st.slider("Number of Questions", 1,10,5)
else:
  question=st.text_area("Enter Interview Question Here!!")
  answere=st.text_area("Enter Your Answere", height=160)
btn=st.button("Generate AI Response")
if btn:
  if mode in ["Evaluate Answeres","Improve the answeres"] and (not question.strip() or (not answere.strip())):
    st.warning("Please Enter a valid Question and Answere")
    st.stop()
  
  if mode =="Generate Questions":
    task="Generate " + str(count) + "Frequently asked Interview questions 3 theoritical and 2 technical. do not give answeres, give hints"
  elif mode =="Generate Code Questions":
    task="Generate " + str(count) + "Frequently asked coding questions on topic" + topic + "and give hint to solve them. be accurate"
  elif mode =="Evaluate Answeres":
    task="question:" + question +"My answere is:" + answere + "Evaluate this answere based on concept,relevent, communication, lenght of answere"
  elif mode =="Improve the Answeres":
    task="question:" + question +"My answere is:" + answere + "Improve this answere based on choice of words, key words include , etc...."
  print(task)
  st.success("Welcome!")
  st.write("Good Morning...")
