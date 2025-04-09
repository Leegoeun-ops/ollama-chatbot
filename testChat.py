import streamlit as st   
from langchain_ollama import ChatOllama # type: ignore

st.header("Hello, It's goony's chatbot test!")

with st.form("llm-form"):
    question = st.text_area("Enter your question:")
    submit = st.form_submit_button("submit")
    
def generate_response(input_text):
    model = ChatOllama(model="llama3.2:1b")
    
    response = model.invoke(input_text)
    
    return response.content

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
if submit and question:
    with st.spinner("Generating response..."):
        response = generate_response(question)
        st.session_state.chat_history.append({"user": question, "ollama": response})
        st.write(response)
        
st.write("## Chat History")
for chat in reversed(st.session_state['chat_history']):
    st.write(f"**User**: {chat['user']}")
    st.write(f"**Assistant**: {chat['ollama']}")
    
    
