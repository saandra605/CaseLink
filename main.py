from pyvis.network import Network
import networkx as nx

G = nx.Graph()

G.add_node("Suspect A", entity_type="suspect", color="red")
G.add_node("Suspect B", entity_type="suspect", color="red")
G.add_node("Victim", entity_type="victim", color="green")
G.add_node("Phone Record", entity_type="evidence", color="blue")
G.add_node("Crime Scene", entity_type="location", color="yellow")

G.add_edge("Suspect A", "Phone Record", relationship="used")
G.add_edge("Phone Record", "Suspect B", relationship="belongs_to")
G.add_edge("Suspect B", "Crime Scene", relationship="visited")
G.add_edge("Crime Scene", "Victim", relationship="last_seen_at")

centrality = nx.degree_centrality(G)

print("\nEntity Importance Scores: ")

for node, score in centrality.items():
    print(f"{node}: {score:.3f}")

most_important = max(centrality, key=centrality.get)

print("\nEntity Types:")

for node, data in G.nodes(data=True):
    print(f"{node}: {data['entity_type']}")

print(f"\nMost Important Entity: {most_important}")
print(f"Score: {centrality[most_important]: .3f}")

net = Network(height="750px", width="100%", notebook=False)

for node, data in G.nodes(data=True):
    net.add_node(node, label=node, color=data["color"])

for source, target in G.edges():
    net.add_edge(source, target)

net.write_html("case_network.html")

print("\nNetwork created!")