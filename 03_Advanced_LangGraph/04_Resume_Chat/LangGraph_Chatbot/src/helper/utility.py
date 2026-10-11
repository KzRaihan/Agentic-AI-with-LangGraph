# **************************************** utility functions *************************
import uuid
import streamlit as st
# Function_1: generated_thread_id
# Purpose: When we call these function then it's automatically generate a random new thread id 
def generated_thread_id():
    thread_id = uuid.uuid4()

    return thread_id

# Function 2: reset_chat()
# Purpose: 1. new chat functionality include
def reset_chat():
    # 1. Generate a new thread id
    thread_id = generated_thread_id()

    # 2. store the new thread id into the session state
    st.session_state['thread_id'] = thread_id

    # 3. Replace the session state old messages to empty (for new chat )
    st.session_state['message_history'] = []

