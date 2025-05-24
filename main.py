from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import feedparser
from newspaper import Article
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

RSS_FEEDS = [
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "https://feeds.bbci.co.uk/news/rss.xml",
    "https://www.aljazeera.com/xml/rss/all.xml"
]

class NewsItem(BaseModel):
    title: str
    summary: str
    relevance: float

def summarize_text(text: str) -> str:
    if not openai.api_key:
        return "Summary unavailable (no API key set)"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": f"Summarize this in 3-4 sentences:\n\n{text}"}],
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Summarization error: {str(e)}"

@app.get("/news", response_model=list[NewsItem])
def get_news():
    results = []
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:3]:
            try:
                article = Article(entry.link)
                article.download()
                article.parse()
                text = article.text[:3000]
                summary = summarize_text(text)
                score = min(len(summary.split()) / 4.0, 10.0)
                results.append(NewsItem(
                    title=entry.title,
                    summary=summary,
                    relevance=round(score, 2)
                ))
            except Exception:
                continue
    return sorted(results, key=lambda x: x.relevance, reverse=True)