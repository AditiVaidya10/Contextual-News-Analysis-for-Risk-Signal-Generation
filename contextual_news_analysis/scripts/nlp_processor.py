
import pandas as pd
import spacy
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")
df = pd.read_csv("data/news_articles.csv")

results = []

for i, row in df.iterrows():
    doc = nlp(row['summary'])
    entities = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in ['ORG', 'PERSON', 'GPE']]
    sentiment = TextBlob(row['summary']).sentiment.polarity
    results.append({
        "title": row['title'],
        "entities": entities,
        "sentiment": sentiment,
        "source": row['source'],
        "published": row['published'],
        "link": row['link']
    })

pd.DataFrame(results).to_json("data/processed_articles.json", orient="records", lines=True)
print("Processed articles saved to data/processed_articles.json")
