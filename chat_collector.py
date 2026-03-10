import pytchat
import json

VIDEO_ID = "YOUR_VIDEO_ID"

chat = pytchat.create(video_id=VIDEO_ID)

chat_data = []

print("Collecting chat...")

while chat.is_alive():
    for c in chat.get().sync_items():
        entry = {
            "user": c.author.name,
            "message": c.message,
            "timestamp": c.datetime
        }
        chat_data.append(entry)
        print(f"{entry['user']}: {entry['message']}")

with open("data/raw_chat.json","w",encoding="utf8") as f:
    json.dump(chat_data,f,indent=4)
