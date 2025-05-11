
import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gexf("data/news_graph.gexf")

# Centrality and influential entities
centrality = nx.degree_centrality(G)
top_nodes = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:5]

print("Top Influential Nodes:")
for node, cent in top_nodes:
    print(f"{node}: {cent:.4f}")

# Visualize subgraph
sub_nodes = [node for node, _ in top_nodes]
subgraph = G.subgraph(sub_nodes)

plt.figure(figsize=(8,6))
nx.draw(subgraph, with_labels=True, node_color='skyblue', edge_color='gray')
plt.title("Top Influential Nodes Subgraph")
plt.savefig("visualizations/top_nodes_subgraph.png")
print("Subgraph visualization saved to visualizations/top_nodes_subgraph.png")
