import json
import pandas as pd
import networkx as nx
from collections import Counter

with open("data/raw_chat.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)
G = nx.Graph()

user_counts = Counter(df["user"])
for user,count in user_counts.items():
    if count > 20:
        G.add_node(user, weight=count)

users = list(G.nodes())
for i in range(len(users)):
    for j in range(i+1,len(users)):
        G.add_edge(users[i], users[j])

nx.write_gexf(G,"data/chat_influencer_network.gexf")
print("Influencer network exported. Open chat_influencer_network.gexf in Gephi.")
