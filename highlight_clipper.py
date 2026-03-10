import pandas as pd

highlights = pd.read_json("data/highlights.json", typ="series")

print("Highlight moments detected:")
for t,v in highlights.items():
    print(t, "message spike:", v)

print("Optionally, install moviepy & pytube to cut video segments around these timestamps.")
