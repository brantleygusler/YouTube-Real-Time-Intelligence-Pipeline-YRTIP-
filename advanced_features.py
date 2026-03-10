import json
import pandas as pd
import re
from collections import Counter

with open("data/raw_chat.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Chat momentum (messages per minute)
df["minute"] = df["timestamp"].dt.floor("T")
momentum = df.groupby("minute").size()
momentum.to_json("data/momentum.json")

# Highlight detection
threshold = momentum.mean() * 3
highlights = momentum[momentum > threshold]
highlights.to_json("data/highlights.json")

# Emoji trends
emoji_pattern = re.compile("[\U00010000-\U0010ffff]", flags=re.UNICODE)
emojis = []
for msg in df["message"]:
    emojis += emoji_pattern.findall(msg)
emoji_counts = Counter(emojis)
with open("data/emojis.json","w") as f:
    json.dump(emoji_counts,f,indent=4)

# Bot detection (users with repeated messages)
bot_candidates = []
user_groups = df.groupby("user")
for user,group in user_groups:
    msgs = group["message"].tolist()
    repeated = len(msgs) - len(set(msgs))
    if repeated > 5:
        bot_candidates.append(user)
with open("data/bots.json","w") as f:
    json.dump(bot_candidates,f,indent=4)

# Viewer segmentation
segments = {}
for user,group in user_groups:
    count = len(group)
    if count > 100:
        segments[user] = "superfan"
    elif count > 20:
        segments[user] = "active"
    elif count > 5:
        segments[user] = "casual"
    else:
        segments[user] = "lurker"
with open("data/segments.json","w") as f:
    json.dump(segments,f,indent=4)

# AI-style stream summary
common_words = Counter(" ".join(df["message"]).lower().split())
summary_words = [w for w,_ in common_words.most_common(20)]
summary = "Chat mostly discussed: " + ", ".join(summary_words)
with open("data/summary.txt","w") as f:
    f.write(summary)

print("Advanced analytics complete.")
