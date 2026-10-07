import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage



# configuration the user thread_id
thread_id = "1"
CONFIG = {
    "configurable":{
        "thread_id": thread_id
        }
    }
    
# to store the user input:
    # we create an dictionary
    # {"role": "user", "content": "hi"}
    # {"role": "assistant", "content": "Hello"}

if 'message_history' not in st.session_state:
    # then assign the message_history with initial null value
    st.session_state['message_history'] = []


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

    with st.chat_message('user'):
        st.text(user_input)


    # 2. AI Response Section
    # import the chatbot object form the backend file
    response = chatbot.invoke({
        "messages": HumanMessage(content=user_input)
    }, config=CONFIG)

    # Extract the AI response only content
    ai_message = response['messages'][-1].content
    
    # append the AI message to the dic
    st.session_state['message_history'].append({"role": "assistant", "content": user_input})
    with st.chat_message('assistant'):
        st.text(ai_message)


# How to run: streamlit run streamlit_frontend.py