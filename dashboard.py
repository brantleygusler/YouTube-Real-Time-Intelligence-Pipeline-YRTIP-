import streamlit as st
import json
import pandas as pd

st.title("YouTube Chat Intelligence Pro Dashboard")

topics = json.load(open("data/topics.json"))
sentiment = json.load(open("data/sentiment.json"))
momentum = pd.read_json("data/momentum.json", typ="series")
highlights = pd.read_json("data/highlights.json", typ="series")
emojis = json.load(open("data/emojis.json"))
bots = json.load(open("data/bots.json"))
segments = json.load(open("data/segments.json"))
summary = open("data/summary.txt").read()

st.header("AI Chat Summary")
st.write(summary)

st.header("Messages Over Time")
st.line_chart(momentum)

st.header("Highlight Moments")
st.write(highlights)

st.header("Top Emojis")
emoji_df = pd.Series(emojis).sort_values(ascending=False).head(20)
st.bar_chart(emoji_df)

st.header("Bot Candidates")
st.write(bots)

st.header("Viewer Segmentation")
seg_df = pd.Series(segments).value_counts()
st.bar_chart(seg_df)

st.header("Chat Topics")
for t,words in topics.items():
    st.subheader(t)
    st.write(", ".join(words))
