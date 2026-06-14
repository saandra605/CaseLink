from pyvis.network import Network
import networkx as nx
import pandas as pd

G = nx.Graph()

entities = pd.read_csv("data/entities.csv")

for index, row in entities.iterrows():  # loop through every row in the table
    G.add_node(row["name"], entity_type=row["entity_type"], color=row["color"])

relationships = pd.read_csv("data/relationships.csv")

for index, row in relationships.iterrows():  # loop through every row in the table
    G.add_edge(row["source"], row["target"], relationship=row["relationship"])

centrality = nx.degree_centrality(G)

print("\nEntity Importance Scores: ")

for node, score in centrality.items():
    print(f"{node}: {score:.3f}")

most_important = max(centrality, key=centrality.get)

def get_score(item):
    return item[1]  # give me the second thing in the item


sorted_entities = sorted(centrality.items(), key=get_score, reverse=True)

print("\nTop Entities:")

rank = 1

for entity, score in sorted_entities:
    print(f"{rank}. {entity}: {score:.3f}")
    rank += 1

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