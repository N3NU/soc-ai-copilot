import streamlit as st
import requests
import uuid

API_URL = "http://localhost:8000/analyze"

st.title("SOC AI Copilot")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Ask a cybersecurity question")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    response = requests.post(
        API_URL,
        json={
            "session_id": st.session_state.session_id,
            "query": prompt
        }
    )

    data = response.json()

    answer = data["answer"]

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.write(answer)