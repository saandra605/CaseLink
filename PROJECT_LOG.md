## Day 1

Built the first version of CaseLink which is a graph-based investigation analysis tool.

Implemented:
- Graph creation using NetworkX
- Interactive visualisation using PyVis
- Entity categories (suspect, victim, witness, evidence, location)
- Relationship modelling between the entities
- Centrality analysis

Learned:
- How nodes and edges work in NetworkX
- How Git and GitHub work
- How to generate an interactive network visually using PyVis

Challenges:
- Setting up Git and GitHub
- Learning how graph-based systems are structured


## Day 2
Can't keep on adding more people, locations or evidence or else the graph would look a mess

Make the software answers questions like:
- Who is most connected?
- Which location appears most often?
- What is the shortest path between A and B

Implemented:
- Ranking entities by their importance

Learned:
- sorting normally goes smallest to largest so you use reverse=True to get the buggest first
- How Pythn functions can be passed as arguments (e.g. key=get_score) to compare tuples

Challenges:
- For ranking entities the centrality score couldn't be sorted correctly because centrality.items() contains tuples so Python would sort the entity by name first not centrality

Next steps:
- Make more realistic case data
- Identify the most important suspect, evidence and location seperately
- Load case data from a CSV file instead of coding it

## Day 3

Implemented:
- A resuable find_most_important() function
- Identified the most important suspect, witness, location and evidence

Changes/Improvements:
- Replaced repeated filtering code with a reusable function

Learned:
- Data filtering
- Sorting custom data structures
- Designing reusable code
- Function parameters

Challenges:
- Understanding how parameters pass values into functions
- Understanding how sorting how sorting functions use key=

Next Steps:
- Community detection
- Larger investigation datasets
- Enhanced analysis features

## Day 4

Implemented:
- Louvain community detection algorithm
- Community-based graph visualisation
- Community assignement for investigation entities

Changes/Improvements:
- Updated the graph colours to represent communities instead od entity types

Learned:
- How the Louvain algorithm idetifies clusters
- How so store and access community IDs for nodes
- How community detection works in graph networks

Challenges:
- Debugging PyVis node creattion errors
- Making sure node colours were updated correctly before generarting the graph
- Understanding what community IDs represent

Next Steps:
- Add hover tool which displays entity type, community ID and importance score
- Make a larger and more realistic investigation dataset
- Test community detection on more complex networks

## Day 5

Implemented:
- Node hover tool
- Displays the entity data within the graph
- Created a larger investigation case: more suspects, witnesses, evidence and location

Changes/Improvements:
- Added entity type display
- Added community ID display
- Added importance score display
- Investigation network is larger and more realistic

Learned:
- How node tooltips work
- How to build a more realistic dataset
- How graph structure affects analysis results

Challenges:
- Fixing tootip formatting
- Debugging graph errors
- Creating realistic relationships between entities

Next Steps:
- Continue improving the investigation analysis

## Day 6

Implemented:
- Addedd betweenness centrality analysis
- Added shortest path analysis between entities

Changes/Improvements:
- Can trace connections between two nodes in the network
- Can find entities that act like a bridge betwen groups

Learned:
- How betweenness centrality works
- How shortest path alorithms find connections in a graph
- The difference between degree centrality and betweenness centrality

Challenges:
- Understanding what information a shortest path funtion needs
- Making analysis function more reusable using parameters
- Converting path lists into a readable output

Next Steps:
- Display shortest paths more clearly in the graph
- Continue improving investigation analysis

## Day 7

Implemented:
- Added entity investigation tool
- Added neighbour relationship display
- Added short path analysis

Changes/Improvements:
- Users can investigate a specific entity
- Investigation results show connected entities and their relationships
- Shortest paths can now explain how entities are connected instead of only showing node names

Learned:
- How to find neighbours of a node
- Why paths contain n - 1 relationships
- How to combine different graph measurements into one function
- How to access edge attributes in NetworkX
- How shortest paths are represented as lists

Challneges:
- Understanding how to work woth neighbouring nodes in a path
- Accessing relationshop information stored on edges
- Designing a reusable investigation function

Next Steps:
-

