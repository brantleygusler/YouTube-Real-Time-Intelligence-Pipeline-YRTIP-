import json

with open("data/topics.json") as f:
    topics = json.load(f)
with open("data/sentiment.json") as f:
    sentiment = json.load(f)

summary = f'''
Stream Recap

Main discussion topics:
{topics}

Audience sentiment:
{sentiment}

Overall, the chat focused heavily on the above themes and reacted strongly during highlight moments.
'''

with open("data/llm_stream_summary.txt","w") as f:
    f.write(summary)

print("LLM-style stream recap saved.")
