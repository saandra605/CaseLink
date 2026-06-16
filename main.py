from pyvis.network import Network
import networkx as nx
import pandas as pd
import community as community_louvain

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

def find_most_important(entity_type):

    importants = []

    for node, data in G.nodes(data=True):
        if data["entity_type"] == entity_type:
            importants.append((node, centrality[node]))

    def get_score(item):
        return item[1]

    sorted_importants = sorted(importants, key=get_score, reverse=True)

    most_important = sorted_importants[0]

    name = most_important[0]
    score = most_important[1]

    print(f"\nMost Important {entity_type.title()}: {name}")
    print(f"Score: {score:.3f}")

find_most_important("suspect")
find_most_important("witness")
find_most_important("location")
find_most_important("evidence")

partition = community_louvain.best_partition(G)

community_colors = {0: "red", 1: "blue", 2: "green", 3: "purple", 4: "orange"}

print("\nCommunitities:")

for node, community_id in partition.items():
    print(f"{node}: Community {community_id}")

net = Network(height="750px", width="100%", notebook=False)

for node in G.nodes():

    community_id = partition[node]

    G.nodes[node]["color"] = community_colors.get(community_id, "grey")

    entity_type = G.nodes[node]["entity_type"]

    importance_score = centrality[node]

    G.nodes[node]["title"] = (f"Type: {entity_type}\n"f"Community: {community_id}\n" f"Importance: {importance_score:.3f}")

net.from_nx(G)

net.write_html("case_network.html")

print("\nNetwork created!")