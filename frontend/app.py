import streamlit as st
import requests

st.set_page_config(page_title="Chat with The Youtuber", layout="wide")

st.title("Chat with The Youtuber")
st.markdown("Ask questions about data engineering topics from The Youtuber's video tutorials!")



user_question = st.text_input("Your question:", placeholder="How do I setup DuckDB?")

if st.button("Send") and user_question != "":
        response = requests.post(
            "http://127.0.0.1:8000/rag/query", json={"prompt": user_question}
        )

        data = response.json()

        st.markdown("## Question:")
        st.markdown(user_question)

        st.markdown("## Answer:")
        st.markdown(data["answer"])

        st.markdown("## Source:")
        st.markdown(data["filepath"])

       
