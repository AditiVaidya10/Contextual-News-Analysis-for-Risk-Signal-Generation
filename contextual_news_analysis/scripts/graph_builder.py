
import json
import networkx as nx
import matplotlib.pyplot as plt

with open("data/processed_articles.json", "r") as f:
    lines = f.readlines()

G = nx.Graph()

for line in lines:
    article = json.loads(line)
    main_title = article['title']
    G.add_node(main_title, type="Article", sentiment=article['sentiment'])

    for ent_text, ent_type in article['entities']:
        G.add_node(ent_text, type=ent_type)
        G.add_edge(main_title, ent_text, relation="mentions")

nx.write_gexf(G, "data/news_graph.gexf")
print("Graph saved to data/news_graph.gexf")
