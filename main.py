from pyvis.network import Network
import networkx as nx
import pandas as pd
import community as community_louvain

G = nx.Graph()

entities = pd.read_csv("data/entities.csv")

for index, row in entities.iterrows():  # loop through every row in the table
    name = row["name"].strip()
    G.add_node(name, entity_type=row["entity_type"], color=row["color"])

relationships = pd.read_csv("data/relationships.csv")

for index, row in relationships.iterrows():  # loop through every row in the table
    G.add_edge(row["source"], row["target"], relationship=row["relationship"], title=row["relationship"])

centrality = nx.degree_centrality(G)

print("\nEntity Importance Scores: ")

for node, score in centrality.items():
    print(f"{node}: {score:.3f}")

betweenness = nx.betweenness_centrality(G)

print("\nBetweenness Scores: ")

for node, score in betweenness.items():
    print(f"{node}: {score:.3f}")

most_important = max(centrality, key=centrality.get)

def get_score(item):
    return item[1]  # give me the second thing in the item


sorted_entities = sorted(centrality.items(), key=get_score, reverse=True)

top_entities = [ ]

for entity, score in sorted_entities[:5]:
    top_entities.append(entity)

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

def find_most_important(entity_type, scores):

    importants = []

    for node, data in G.nodes(data=True):
        if data["entity_type"] == entity_type:
            importants.append((node, scores[node]))

    def get_score(item):
        return item[1]

    sorted_importants = sorted(importants, key=get_score, reverse=True)

    most_important = sorted_importants[0]

    name = most_important[0]
    score = most_important[1]

    print(f"\nMost Important {entity_type.title()}: {name}")
    print(f"Score: {score:.3f}")

    return name

most_important_suspect = find_most_important("suspect", centrality)

most_important_witness = find_most_important("witness", centrality)

most_important_location = find_most_important("location", centrality)

most_important_evidence = find_most_important("evidence", centrality)

most_important_entity = most_important

def find_shortest_path(start, end):

    list = nx.shortest_path(G, start, end)

    print(f"\nShortest Path from {start} -> {end} is: ")

    for i in range(len(list) - 1):
        node1 = list[i]
        node2 = list[i + 1]

        relationship = G[node1][node2]["relationship"]

        print(f"{node1} -- {relationship} --> {node2}")


find_shortest_path("John Carter","Marcus White")

partition = community_louvain.best_partition(G)

def investigate(entity):

    entity_type = G.nodes[entity]["entity_type"]

    community = partition[entity]
    degree = centrality[entity]
    between = betweenness[entity]
    neighbors = list(G.neighbors(entity))


    print(f"\nEntity: {entity}")
    print(f"Type: {entity_type}")
    print(f"\nNeighbours: ")

    for neighbor in neighbors:
        relationship = G[entity][neighbor]["relationship"]
        print(f"- {neighbor} ({relationship})")

    print(f"\nCommunity: {community}")
    print(f"Degree Centrality: {degree}")
    print(f"Betweeness: {between}")

investigate("Marcus White")

def get_entity_info(entity):

    entity_type = G.nodes[entity]["entity_type"]

    community = partition[entity]

    degree = centrality[entity]

    between = betweenness[entity]

    neighbours = [ ]

    for neighbour in G.neighbors(entity):
        relationship = G[entity][neighbour]["relationship"]

        neighbours.append({"name": neighbour, "relationship": relationship})

    return {
        "entity": entity,
        "type": entity_type,
        "community": community,
        "degree": degree,
        "betweenness": between,
        "neighbours": neighbours
    }

print(get_entity_info("Marcus White"))


community_colors = {0:"#4C78A8", 1: "#F58518", 2: "#54A24B", 3: "#B279A2", 4: "#E45756",}

print("\nCommunitities:")

for node, community_id in partition.items():
    print(f"{node}: Community {community_id}")

total_entities = len(G.nodes())
total_relationships = len(G.edges())
total_communities = len(set(partition.values()))

def get_entities_by_type(entity_type):

    entities = []

    for node, data in G.nodes(data=True):

        if data["entity_type"] == entity_type:
            entities.append((node, centrality[node]))

    entities = sorted(entities, key=get_score, reverse=True)

    return [entity for entity, score in entities]

def get_entity_count(entity_type):

    count = 0

    for node, data in G.nodes(data=True):

        if data["entity_type"] == entity_type:
            count += 1

    return count

total_suspects = get_entity_count("suspect")
total_witnesses = get_entity_count("witness")
total_evidence = get_entity_count("evidence")
total_locations = get_entity_count("location")
total_vehicles = get_entity_count("vehicle")
total_organisations = get_entity_count("organisation")

def create_filtered_graph(entity_type):

    filtered_graph = nx.Graph()

    for node, data in G.nodes(data=True):

        if data["entity_type"] == entity_type:

            filtered_graph.add_node(node, **data)
    for node1, node2, data in G.edges(data=True):

        if node1 in filtered_graph.nodes() and node2 in filtered_graph.nodes():

            filtered_graph.add_edge(node1, node2, **data)
    return filtered_graph

def create_graph(entity_filter="all", selected_entity=None):

    net = Network(height="750px", width="100%", notebook=False)

    for node in G.nodes():

        community_id = partition[node]

        entity_type = G.nodes[node]["entity_type"]

        original_color = community_colors.get(community_id, "grey")

        if node == selected_entity:
            G.nodes[node]["color"] = "#FFD700"


        elif entity_filter == "all":
            G.nodes[node]["color"] = original_color

        elif G.nodes[node]["entity_type"] == entity_filter:
            G.nodes[node]["color"] = original_color

        else:
            G.nodes[node]["color"] = "#d3d3d3"
        importance_score = centrality[node]

        G.nodes[node]["title"] = (f"Entity: {node}\n"
                                  f"Type: {entity_type}\n"
                                  f"Community: {community_id}\n"
                                  f"Importance: {importance_score:.3f}\n"
                                  f"Betweenness: {betweenness[node]:.3f}")

        G.nodes[node]["size"] = 15 + (centrality[node] * 100)

        if node == selected_entity:
            G.nodes[node]["font"] = {"size": 22, "bold": True}
        else:
            G.nodes[node]["font"] = {"size": 14}

    net.from_nx(G)

    net.show_buttons()

    net.write_html("case_network.html")