from pyvis.network import Network
import networkx as nx

G = nx.Graph()

# Suspects
G.add_node("John Carter", entity_type="suspect", color="red")
G.add_node("Lisa Green", entity_type="suspect", color="red")

# Victim
G.add_node("Emma Brown", entity_type="victim", color="green")

# Witness
G.add_node("Michael Reed", entity_type="witness", color="orange")

# Location
G.add_node("Warehouse", entity_type="location", color="yellow")
G.add_node("Train Station", entity_type="location", color="yellow")

# Evidence
G.add_node("Phone Record #19", entity_type="evidence", color="blue")
G.add_node("Fingerprint A12", entity_type="evidence", color="blue")

G.add_edge("John Carter", "Phone Record #19", relationship="used")
G.add_edge("Phone Record #19", "Lisa Green", relationship="belongs_to")
G.add_edge("Lisa Green", "Warehouse", relationship="visited")
G.add_edge("Fingerprint A12", "Warehouse", relationship="found_at")
G.add_edge("Emma Brown", "Warehouse", relationship="last_seen_at")
G.add_edge("Fingerprint A12", "John Carter", relationship="linked_to")
G.add_edge("Michael Reed", "Train Station", relationship="seen_at")
G.add_edge("Michael Reed", "Emma Brown", relationship="saw")

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