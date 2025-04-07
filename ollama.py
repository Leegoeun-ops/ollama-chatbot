import streamlit as st
import pandas as pd
import numpy as np
import math
import random
import streamlit as st
from langchain_ollama import ChatOllama # type: ignore

st.header("Hello, It's goony's chatbot test!")

with st.form("llm-form"):
    question = st.text_area("Enter your question:")
    submit = st.form_submit_button("submit")
    
def generate_response(input_text):
    model = ChatOllama(model="llama3.2:1b")
    
    response = model.invode(input_text)
    
    return response.content

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
if submit and question:
    with st.spinner("Generating response..."):
        response = generate_response(question)
        st.session_state.chat_history.append({"user": question, "ollama": response})
        st.write(response)
        
st.write("## Chat History")
for chat in st.session_state['chat_history']:
    st.write(f"**User**: {chat['user']}")
    st.write(f"**Assistant**: {chat['ollama']}")
    
    



# image = st.file_uploader("Upload an Inage:", type=["jpg", 'jpeg', 'png'])
# if image:
#     st.image(image=image, width = 500)

# st.write('Hi!')
# st.title("Make Your Own Chat Bot")

# st.subheader("subheader")

# st.text("text")

# st.write("default font")

# st.markdown("This is markdown")
# st.markdown("# This is markdown heading")
# st.markdown("## This is markdown subheading")

# name = st.text_area("Enter your name")

# button = st.button("Click Me")
# if button:
#     st.write("Clicked Btn")
    
# json_data = {
#     "name" : "Test",
#     "age" : 30
# }

# df = pd.read_csv("data/example")

# import firebase_admin
# from firebase_admin import credentials, db
 
# # Initialize Firebase
# cred = credentials.Certificate('path/to/serviceAccountKey.json')
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://your-database-url.firebaseio.com'
# })
 
# # Get a reference to the database
# ref = db.reference('/')
 
# # Read data
# print(ref.get())