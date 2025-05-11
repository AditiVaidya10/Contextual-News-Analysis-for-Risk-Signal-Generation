
import feedparser
import pandas as pd

rss_feeds = {
    "Reuters": "http://feeds.reuters.com/reuters/businessNews",
    "BBC": "http://feeds.bbci.co.uk/news/world/rss.xml",
    "Al Jazeera": "https://www.aljazeera.com/xml/rss/all.xml",
    "Channel News Asia": "https://www.channelnewsasia.com/rssfeeds/8395952"
}

articles = []

for source, url in rss_feeds.items():
    feed = feedparser.parse(url)
    for entry in feed.entries[:20]:
        articles.append({
            "source": source,
            "title": entry.get("title", ""),
            "summary": entry.get("summary", ""),
            "published": entry.get("published", ""),
            "link": entry.get("link", "")
        })

df = pd.DataFrame(articles)
df.to_csv("data/news_articles.csv", index=False)
print("News articles saved to data/news_articles.csv")
