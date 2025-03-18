import streamlit as st
import requests

# Use internal FastAPI URL since both run in the same container
API_URL = "http://localhost:8000"

st.title("📢 News Summarization & Sentiment Analysis")

# Fetch news
company = st.text_input("Enter a company name:")
if st.button("Fetch News"):
    response = requests.get(f"{API_URL}/fetch_news/?company={company}")

    if response.status_code == 200:
        data = response.json()
        if "error" in data:
            st.error(data["error"])
        else:
            st.subheader(f"📰 News Summary for {company}")

            for i, article in enumerate(data["articles"], start=1):
                st.write(f"**{i}. {article['title']}**")
                st.write(f"**Summary:** {article['summary']}")
                st.write(f"**Sentiment:** {article['sentiment']}")
                st.write("---")

            st.subheader("📊 Sentiment Distribution")
            st.write(data["sentiment_analysis"]["Sentiment Distribution"])
    else:
        st.error("Failed to fetch news.")

# Hindi TTS
st.subheader("🔊 Generate Hindi Speech")
hindi_text = st.text_area("Enter Hindi text for speech synthesis:")

if st.button("Generate Hindi TTS"):
    response = requests.post(f"{API_URL}/generate_tts/", data={"hindi_text": hindi_text})
    
    if response.status_code == 200:
        tts_file = response.json()["audio_file"]
        st.audio(tts_file, format="audio/mp3")
    else:
        st.error("Failed to generate TTS.")
