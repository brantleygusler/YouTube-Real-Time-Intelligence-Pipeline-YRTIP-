import json
import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from nltk.sentiment import SentimentIntensityAnalyzer

with open("data/raw_chat.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Save user activity counts
user_counts = df["user"].value_counts()
user_counts.to_json("data/users.json")

# Clean chat messages
def clean(text):
    text = text.lower()
    text = re.sub(r"http\S+","",text)
    text = re.sub(r"[^a-z\s]","",text)
    return text

df["clean"] = df["message"].apply(clean)

# Topic modeling
vectorizer = CountVectorizer(stop_words="english", min_df=5)
X = vectorizer.fit_transform(df["clean"])

lda = LatentDirichletAllocation(n_components=6, random_state=42)
lda.fit(X)

words = vectorizer.get_feature_names_out()
topics = {}
for i,topic in enumerate(lda.components_):
    top_words = [words[j] for j in topic.argsort()[-10:]]
    topics[f"Topic {i+1}"] = top_words

with open("data/topics.json","w") as f:
    json.dump(topics,f,indent=4)

# Sentiment analysis
sia = SentimentIntensityAnalyzer()
df["sentiment"] = df["message"].apply(lambda x: sia.polarity_scores(x)["compound"])

sentiment_summary = {
    "positive": len(df[df.sentiment > 0.2]),
    "neutral": len(df[(df.sentiment >= -0.2) & (df.sentiment <= 0.2)]),
    "negative": len(df[df.sentiment < -0.2])
}

with open("data/sentiment.json","w") as f:
    json.dump(sentiment_summary,f,indent=4)

print("Chat analysis complete.")
