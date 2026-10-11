import streamlit as st
from src.backend.langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

from src.helper.utility import generated_thread_id, reset_chat
    
    
# **************************************** Session Setup ******************************
if 'message_history' not in st.session_state:
    # then assign the message_history with initial null value
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    # set the dynamic thread_id in the session state
    st.session_state['thread_id'] = generated_thread_id()


# **************************************** Sidebar UI *********************************
# Step_1:
st.sidebar.title("LangGraph Chatbot")

if st.sidebar.button("New Chat"):
    reset_chat()

st.sidebar.header("My Conversion")

# step 2
st.sidebar.text(st.session_state['thread_id'])





# **************************************** Main UI ************************************
# Loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input("Type Here")

# if user input is set
if user_input:
    # 1. User Section
    # append the user message to the dic
    st.session_state['message_history'].append({"role": "user", "content": user_input})

    # for Display the user message
    with st.chat_message('user'):
        st.text(user_input)

    # now dynamically set the thread_id into config
    CONFIG = {
    "configurable":{
        "thread_id": st.session_state['thread_id']
        }
    }
    # 2. AI Response Section
    with st.chat_message('assistant'):
        ai_message = st.write_stream(
                message_chunk.content for message_chunk, metadata in chatbot.stream(
                    {
                        "messages": [ HumanMessage(content=user_input)]         
                                
                    },
                    config = CONFIG,
                    stream_mode="messages"
                )
            )
        

    # append the AI message to the dic
    st.session_state['message_history'].append({"role": "assistant", "content": ai_message})
    


# How to run: streamlit run streamlit_frontend.py