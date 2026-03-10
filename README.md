# YouTube Chat Intelligence Pro

A data science platform that analyzes YouTube livestream chat and turns audience conversations into actionable insights.

The system collects chat messages in real time, performs natural language processing, detects behavioral patterns in viewers, and visualizes results through an analytics dashboard.

This project demonstrates a full data pipeline including scraping, NLP analysis, behavioral segmentation, and data visualization.

---

## Features

Chat Collection
- Collects livestream chat using pytchat
- Stores messages by user handle with timestamps

Natural Language Processing
- Topic modeling to detect what chat is discussing
- Sentiment analysis to measure audience mood
- AI-style stream recap generation

Audience Analytics
- Viewer segmentation (superfans, active users, casual users, lurkers)
- Bot detection through repeated message analysis
- Influencer detection through network graphs

Engagement Analysis
- Chat momentum tracking (messages per minute)
- Highlight moment detection during spikes in activity
- Emoji trend tracking

Visualization
- Interactive analytics dashboard built with Streamlit
- Charts for engagement, sentiment, topics, and user activity

Advanced Insights
- Highlight timestamps for potential video clips
- Influencer network graphs exportable to Gephi
- Stream discussion summaries

---

## Project Structure

youtube-chat-intelligence-pro/

chat_collector.py  
Collects live chat messages from a YouTube livestream

chat_analyzer.py  
Performs NLP topic modeling and sentiment analysis

advanced_features.py  
Detects engagement spikes, emoji trends, bots, and viewer segments

highlight_clipper.py  
Finds highlight timestamps where chat activity spikes

llm_summary.py  
Generates a readable summary of chat discussion

influencer_graph.py  
Builds a network graph of high-activity chat participants

dashboard.py  
Interactive analytics dashboard using Streamlit

data/  
Stores generated datasets and analytics results

README.md

---

## Installation

Clone the repository

git clone https://github.com/yourusername/youtube-chat-intelligence-pro

cd youtube-chat-intelligence-pro


Install dependencies


pip install pytchat pandas scikit-learn nltk streamlit networkx


Download the sentiment analysis model


python -c "import nltk; nltk.download('vader_lexicon')"


---

## Running the Pipeline

Step 1 – Collect chat data


python chat_collector.py


Step 2 – Run NLP analysis


python chat_analyzer.py


Step 3 – Run advanced behavioral analytics


python advanced_features.py


Step 4 – Detect highlight moments


python highlight_clipper.py


Step 5 – Generate stream recap


python llm_summary.py


Step 6 – Generate influencer network graph


python influencer_graph.py


Step 7 – Launch dashboard


streamlit run dashboard.py


---

## Example Insights

Chat Sentiment
Positive: 62%  
Neutral: 27%  
Negative: 11%

Top Topics
- game strategy
- funny moments
- stream announcements
- patch updates

Viewer Segments
Superfans: 18  
Active: 142  
Casual: 390  
Lurkers: 2200

Highlight Moment
12:44:03 — 2,100 messages per minute spike

Top Emojis
🔥 😂 💀 🎉

---

## Technologies Used

Python  
pytchat  
scikit-learn  
NLTK  
Pandas  
NetworkX  
Streamlit  

---

## Use Cases

Creator Analytics
Understand audience reactions during livestreams.

Marketing Intelligence
Identify which moments and topics drive engagement.

Community Analysis
Discover influencers and highly engaged fans.

Content Optimization
Detect highlight moments for clips and social media.

---

## Future Improvements

Automatic video highlight clipping from livestream recordings

Real-time meme detection in chat

Machine learning models for predicting engagement spikes

Live dashboards during active streams

---

## Portfolio Value

This project demonstrates skills in:

Data scraping  
Natural language processing  
Machine learning  
Behavioral analytics  
Network analysis  
Data visualization  

It represents a full end-to-end analytics pipeline for social media audience intelligence.

---
