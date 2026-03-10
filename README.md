# YouTube-Real-Time-Intelligence-Pipeline-YRTIP

**Transform livestream chat into actionable audience insights**

This project collects, analyzes, and visualizes YouTube livestream chat using 
Python, NLP, and behavioral analytics. It provides insights on topics, sentiment, 
engagement spikes, viewer segmentation, bots, emoji trends, influencer networks, and 
generates AI-style stream recaps.

## Features

- **Chat Collection**: Real-time messages stored by user handle
- **NLP Analysis**: Topic modeling and sentiment analysis
- **Behavioral Analytics**: Viewer segmentation, bot detection, emoji trends
- **Engagement Analytics**: Chat momentum, highlight moments
- **Advanced Insights**: Influencer network, AI-style stream summaries
- **Interactive Dashboard**: Built with Streamlit

## Technologies 
Python, pytchat, pandas, scikit-learn, NLTK, NetworkX, Streamlit

## Installation

```bash
pip install pytchat pandas scikit-learn nltk streamlit networkx
python -c "import nltk; nltk.download('vader_lexicon')"
