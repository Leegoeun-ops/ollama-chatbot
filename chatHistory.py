import streamlit as st   
from langchain_ollama import ChatOllama # type: ignore
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate
from langchain_core.prompts import ChatPromptTemplate

model = ChatOllama(model="llama3.2:1b")

system_message = SystemMessagePromptTemplate.from_template("You are a helpful AI Assistant. You work as teacher for 5th grade students. You explain things in short and brief.")

st.header("Hello, It's goony's chatbot history test!")

if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

with st.form("llm-form"):
    question = st.text_area("Enter your question:")
    submit = st.form_submit_button("submit")

def generate_response(chat_history):
    
    chat_template = ChatPromptTemplate.from_messages(chat_history)
    
    chain = chat_template|model|StrOutputParser()
    response = chain.invoke({})
    
    return response
    
def get_history():
    chat_history = [system_message]
    for chat in st.session_state['chat_history']:
        human_message = HumanMessagePromptTemplate.from_template(chat['user'])
        chat_history.append(human_message)
        
        ai_message = AIMessagePromptTemplate.from_template(chat['assistant'])
        chat_history.append(ai_message)
        
    return chat_history

if submit and question:
    with st.spinner("Generating response..."):
        message = HumanMessagePromptTemplate.from_template(question)
        
        chat_history = get_history()
        
        chat_history.append(message)
        
        response = generate_response(chat_history)
        
        st.session_state['chat_history'].append({'user': question, 'assistant': response})
        
st.write("## Chat History")

for chat in reversed(st.session_state['chat_history']):
    st.write(f"**:adult: User**: {chat['user']}")
    st.write(f"**:brain: Assistant**: {chat['assistant']}")
    