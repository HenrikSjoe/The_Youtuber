import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = f"https://the-youtuber-hs-de24.azurewebsites.net/rag/query?code={os.getenv('FUNCTION_APP_API')}"

user_question = st.text_input("Your question:", placeholder="How do I setup DuckDB?")

if st.button("Ask The Youtuber"):
    if user_question:
        with st.spinner("Searching video transcripts..."):
            try:
                response = requests.post(url, json={"prompt": user_question})
                
                if response.status_code == 200:
                    data = response.json()
                    
                    st.success("Answer found!")
                    
                    col1, col2 = st.columns([2, 1])
                    
                    with col1:
                        st.subheader("Answer")
                        st.write(data['answer'])
                    
                    with col2:
                        st.subheader("Source")
                        st.info(f"**Video:** {data['video_title']}")
                        with st.expander("Show file path"):
                            st.code(data['filepath'])
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except requests.exceptions.ConnectionError:
                st.error("Cannot connect to API. Verify your internet connection and FUNCTION_APP_API key.")
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a question")
