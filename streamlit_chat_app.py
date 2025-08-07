# streamlit_chat_app.py

import streamlit as st
from agent import agent_executor # Import our agent from agent.py

st.set_page_config(page_title="AI Health Agent", layout="wide")
st.title("👩‍⚕️ AI Health Agent")
st.info("I'm an AI agent designed to help analyze symptoms. Please describe how you're feeling.")

# Initialize chat history in Streamlit's session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("How are you feeling today?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get the agent's response
    with st.spinner("Thinking..."):
        response = agent_executor.invoke({"input": prompt})
        response_content = response['output']

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response_content)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response_content})