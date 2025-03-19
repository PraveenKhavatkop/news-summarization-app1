import streamlit as st
import requests

st.title("📢 News Summarization & Sentiment Analysis")

API_URL = "http://127.0.0.1:8000"

### FETCH NEWS ARTICLES ###
company = st.text_input("Enter a company name:", "Tesla")

if st.button("Fetch News"):
    response = requests.post(f"{API_URL}/fetch_news/", json={"company_name": company})
    
    if response.status_code != 200:
        st.error("Failed to fetch news. Try again.")
    else:
        data = response.json()
        
        if "error" in data:
            st.error("No articles found.")
        else:
            st.subheader(f"📰 News Summary for {company}")

            for i, article in enumerate(data["articles"]):
                st.write(f"**{i+1}. {article['title']}**")
                st.write(f"**Summary:** {article['summary']}")
                st.write(f"**Sentiment:** {article['sentiment']}")
                st.write(f"🔗 [Read More]({article['url']})")
                st.write("---")

            # Play Hindi Speech Output
            st.subheader("🔊 Hindi Speech Output (Summary)")
            st.audio("news_summary.mp3", format="audio/mp3")

### HINDI TEXT-TO-SPEECH ###
st.subheader("🔊 Enter Hindi Text for Speech")
hindi_text = st.text_area("Enter Hindi text:", "यह एक उदाहरण पाठ है।")

if st.button("Generate Hindi Speech"):
    response = requests.post(f"{API_URL}/generate_tts/", json={"text": hindi_text})
    
    if response.status_code == 200:
        st.audio("hindi_speech.mp3", format="audio/mp3")
    else:
        st.error("Failed to generate speech.")
