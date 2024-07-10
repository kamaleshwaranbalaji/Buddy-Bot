import os
import streamlit as st
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage


api_key = os.environ.get("MISTRAL_API_KEY")
model = "mistral-large-latest"


client = MistralClient(api_key=api_key)

import streamlit as st
st.title("Buddybot")

user_input = st.text_input("Enter your question:", "ask me something....")

if st.button("submit"):
    with st.spinner("Getting response..."):
        messages = [ChatMessage(role="user", content=user_input)]
        chat_response = client.chat(model=model, messages=messages)
        response = chat_response.choices[0].message.content
        st.text_area("Response", response, height=200)
