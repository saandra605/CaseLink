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