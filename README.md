# News Summarization & Text-to-Speech App

## Overview
This app extracts news articles for a given company, summarizes them, performs sentiment analysis, and converts the Hindi text into **Hindi speech**. 

## Features
✅ Fetches **10 news articles** related to a company  
✅ Analyzes the **sentiment** of each article  
✅ Compares **sentiment trends** across articles  
✅ Converts summarized text into **Hindi speech**  
✅ **User-friendly interface** with Streamlit  
✅ **API for fetching news & generating speech**  
✅ **Deployed on Hugging Face Spaces**

## Technologies Used
📝 **Web Scraping**: `BeautifulSoup`, `requests`
🔍 **Sentiment Analysis**: `TextBlob`, `VADER`
🔊 **Text-to-Speech**: `gTTS`
🌐 **Web Framework**: `Streamlit`
🚀 **API Development**: `FastAPI`
☁️ **Deployment**: `Hugging Face Spaces`

## Installation & Setup
### 📌 Prerequisites
🔹 Install **Python 3.8+**  
🔹 Install dependencies:
```bash
pip install -r requirements.txt
```

### ▶️ Running the Application
```bash
# Start the FastAPI backend
uvicorn api:app --reload

# Start the Streamlit frontend
streamlit run app.py
```

## API Endpoints
📌 **Fetch News**  
```http
GET /fetch_news/?company=<company_name>
```
📌 **Generate Hindi Speech**  
```http
POST /generate_tts/
Payload: {"hindi_text": "Your text here"}
```

## Project Structure
```
📂 news-summarization-app
│-- app.py          # Streamlit UI
│-- api.py          # FastAPI Backend
│-- utils.py        # Helper functions (scraping, sentiment, TTS)
│-- requirements.txt # Dependencies
│-- README.md       # Documentation
```

## Deployment
🚀 Live Demo: [Hugging Face Spaces](https://huggingface.co/spaces/praveen19969/news-summarization-tts)

---
💡 *Simple, Fast, and Effective!*

