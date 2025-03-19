## News Summarization and Text-to-Speech App

### Overview

This project extracts news articles related to a given company, summarizes them, performs sentiment analysis, and converts the summarized text into Hindi speech. The application provides a web-based interface for user interaction and is deployed on Hugging Face Spaces.

### Features

Extracts news articles using web scraping

Summarizes news content

Performs sentiment analysis (Positive, Negative, Neutral)

Converts summarized text to Hindi speech

Provides a user-friendly web interface

Backend API for data processing

### Technologies Used

Web Scraping: BeautifulSoup, Requests

Sentiment Analysis: TextBlob 

Text-to-Speech (TTS): gTTS

Web Framework: Streamlit

API Development: FastAPI

Deployment: Hugging Face Spaces

Installation

### Clone the repository:

git clone https://github.com/PraveenKhavatkop/news-summarization-app1.git
cd news-summarization-app

### Install dependencies:

pip install -r requirements.txt

## Run the application:

streamlit run app.py  # If using Streamlit

### API Endpoints

Fetch News: /api/news?company=<company_name>

Text-to-Speech Conversion: /api/tts

### Deployment

The application is deployed on Hugging Face Spaces:
Live Demo

## Project Structure
📂 news-summarization-app

│-- app.py         # Main application file / Frontend

│-- api.py         # API endpoints / Backend

│-- utils.py       # Helper functions

│-- requirements.txt  # Dependencies

│-- README.md      # Project documentation
