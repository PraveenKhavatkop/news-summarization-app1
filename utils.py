import requests
from bs4 import BeautifulSoup
from newspaper import Article
import concurrent.futures  # Enables parallel processing

def fetch_article(url):
    """Fetches and processes a single news article."""
    try:
        news_article = Article(url)
        news_article.download()
        news_article.parse()

        if news_article.title and news_article.text:
            return {
                "title": news_article.title,
                "url": url,
                "summary": news_article.text[:500]  # Get first 500 characters
            }
    except Exception:
        return None

def get_news_articles(company_name, num_articles=10):
    """Fetches exactly 10 news articles quickly using parallel processing."""
    search_url = f"https://www.bing.com/news/search?q={company_name}&FORM=HDRSC6"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    article_links = [link["href"] for link in soup.find_all("a", href=True) if "http" in link["href"]]

    # Ensure we get at least 15 links to avoid missing articles
    article_links = list(set(article_links))[:15]  # Remove duplicates and limit to 15

    news_data = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(fetch_article, article_links)  # Parallel fetching

    for result in results:
        if result:
            news_data.append(result)
        if len(news_data) >= num_articles:
            break

    # Ensure exactly 10 articles (fill empty slots if needed)
    while len(news_data) < num_articles:
        news_data.append({
            "title": "No News Found",
            "url": "N/A",
            "summary": "No relevant news found for this company."
        })

    return news_data[:num_articles]




from textblob import TextBlob

def analyze_sentiment(text):
    """Classifies sentiment based on polarity score."""
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

def compare_sentiments(articles):
    """Creates a structured sentiment report."""
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}

    for article in articles:
        sentiment_counts[article["sentiment"]] += 1

    return {
        "Sentiment Distribution": sentiment_counts,
        "Impact Analysis": [
            {
                "Comparison": f"{articles[0]['title']} vs {articles[1]['title']}",
                "Impact": "Different perspectives on the same topic."
            } if len(articles) > 1 else {}
        ]
    }


from gtts import gTTS
import os

def generate_hindi_tts(hindi_text, output_file="static/audio/output.mp3"):
    """Generates Hindi speech from user input."""
    tts = gTTS(text=hindi_text, lang="hi")
    os.makedirs("static/audio", exist_ok=True)  # Ensure directory exists
    tts.save(output_file)
    return output_file

