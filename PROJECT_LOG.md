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

## Day 8

Implemented:
- Added node information popups
- Added relationship popups on graph connections
- Added node sizing based on their importance scores

Changes/Improvements:
- Hovering over a node now shows investigation information
- Hovering over a connection shows the relationship type
- Graph is easier to understand visually

Learned:
- How to add extra information to PyVis nodes
- How to add information to graph connections
- How to change node sizes automatically

Challenges:
- Getting information to display correctly on the graph
- Trying to get PyVis control buttons to appear

Next Steps:
- Make the graph more interactive
- Move investigation tools onto the webpage
- Adding a search functionality

## Day 9

Implemented:
- Created a Flask web application
- Added HTML templates
- Embedded PyVis graph into the website

Changes/Improvements:
- CaseLink can be accessed through a web browser
- The graph is displayed directly on the website

Learned:
- How Flask routes work
- How HTML templates work
- How to serve files through Flask

Challenges:
- Fixing the render_template error
- Understanding send_file()
- Getting the graph to display correctly inside the webpage

Next Steps:
- Improve the website layout
- Add navigation buttons

## Day 10

Implemented:
- Added Top Entities section to the website
- Added Case Summary section to the website
- Added Entity Investigation section to the website
- Connected graph analysis data from main.py to Flask
- Created a get_entity_info() function

Changes/Improvements:
- Analysis results are displayed on the website instead of only in the terminal

Learned:
- How to import variables and functions between Python files
- How to pass data from Flask to HTML
- How Flask template loops work
- The difference between printing data and returning data

Challenges:
- Fixing the sorted vs sorted_entities error
- Understanding how data moves from Python to Flask and then to HTML
- Learning how to display dictionary values in templates

Next Steps:
- Add entity search functionality
- Allow users to investigate different entities
- Display neighbour relationships on the website
- Improve the website layout and design

## Day 11

Implemented:
- Added entity search functionality
- Connected the user input to graph analysis
- Added a dashboard-style webpage layout
- Added information cards for analysis sections
- Added a sidebar and graph layout

Changes/Improvements:
- Users can search for entities directly from the website
- Investigation information updates automatically
- Website layout is more organised and easier to use
- Graph is now displayed alongside investigation information

Learned:
- How HTML forms work
- How to use request.args in Flask
- How to receive user input from webpages
- How to create dashboard layouts using CSS
- How to organise webpage content into sections

Challenges:
- Fixing the entity variable error
- Debugging the search box
- Understanding how Flask handles form input

Next Steps:
- Imrpove the overall user interface

## Day 12

Implemented:
- Redesigned the CaseLink dashboard
- Added a professional header
- Improved the overall website layout
- Improved the search bar design
- Improved card styling anf spacing

Changes/Improvements:
- Dashboard has a cleaner and more professional appearance
- Search functionality is easier to use
- Investigation graph is presented more clearly alongside the dashboard

Learned:
- How CSS can improve the appearance of a web application
- How Flexbox can be used to build dashboard layouts
- How to organise information into reusable interface components

Challenges:
- Debugging CSS layout issues
- Improving the dashboard without changing the existing functionality
- Balancing the sidebar and graph layout

## Day 13

Implemented:
- Added entity filtering to the dashboard
- Added filter buttons for different entity types
- Added a reusable get_entities_by_type() function
- Ranked the filtered entities by their importance scores

Changes/Improvements:
- Users can filter entities by type (suspects, witnesses, evidence, locations, vehicles and organisations)
- Filtered results are now sorted by importance instead of the order they were added

Learned:
- How to filter data using reusable Python functions
- How to pass filter values from HTML to Flask using URL parameters
- How to sort filtered data before displaying it

Challenges:
- Understanding why sorting required both entity names and centrality scores
- Fixing tuple and list errors when sorting filtered entities

## Day 14

Implemented:
- Added entity-type filtering to the investigation network
- Added graph highlighting based on the selected entity type
- Added an "All" option to display the full network
- Kept non-selected entities visible but faded to keep the network context

Changes/Improvements:
- Users can now focus on specific types of entities within the investigation network
- The graph is easier to analyse when there are many different entity types

Learned:
- How to pass a filter from the website to Python
- How to change the colour of graph nodes
- How to use if statements to control what appears on the graph
- How Flask and PyVis can work together

Challenges:
- Getting the filter to work correctly with the graph
- Making sure the graph updated when a different filter was selected
- Fixing an error with variables being imported from main.py

## Day 15

Implemented:
- Added a clearer display for the entity currently being investigated
- Removed the duplicate entity name from the investigation section
- Improved the styling of the current entity display

Changes/Improvements:
- Removed unnecessary repetition from the investigation results
- Made the dashboard cleaner and easier to read

Learned:
- How to use CSS classes to style specific sections of a webpage
- How HTML structure affects how information is displayed

Challenges:
- Finding where the duplicate entity name was being displayed
- Changing the investigation section without affecting the rest of the dashboard

## Day 16

Implemented:
- Highlighted the entity currently being investigated in the graph
- Improved community colours
- Improved entity labels
- Added a network legend explaining graph colours

Changes/Improvements:
- The searched entity is now highlighted in yellow
- Community colours are less harsh
- The currently investigated entity has a larger, bold label
- Added a network legend to explain community colours, selected entities and filtered entities

Learned:
- How URL parameters can be used to pass the selected entity to the graph
- How HTML and CSS can be used to create a network legend

