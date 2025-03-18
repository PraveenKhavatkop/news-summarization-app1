from fastapi import FastAPI, Form
from utils import get_news_articles, analyze_sentiment, compare_sentiments, generate_hindi_tts

app = FastAPI()

@app.get("/fetch_news/")
def fetch_news(company: str):
    """Fetches 10 news articles and analyzes sentiment."""
    articles = get_news_articles(company)
    if not articles:
        return {"error": "No articles found"}

    for article in articles:
        article["sentiment"] = analyze_sentiment(article["summary"])

    sentiment_comparison = compare_sentiments(articles)
    return {"company": company, "articles": articles, "sentiment_analysis": sentiment_comparison}

@app.post("/generate_tts/")
def generate_tts(hindi_text: str = Form(...)):
    """Generates Hindi speech from user input."""
    tts_file = generate_hindi_tts(hindi_text)
    return {"audio_file": tts_file}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
