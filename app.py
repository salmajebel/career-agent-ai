import streamlit as st
from agent import ask_agent

st.set_page_config(page_title="CareerAgent Chat", layout="wide")

st.title("🧠 CareerAgent Chat")

# historique chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# afficher messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# input chat
user_input = st.chat_input("Ask your CareerAgent...")

if user_input:

    # user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # AI response
    response = ask_agent(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.write(response)
