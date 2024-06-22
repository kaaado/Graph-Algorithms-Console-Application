# Graph Algorithms Console Application

This repository contains a console application for visualizing and performing various graph algorithms. The application allows users to input graphs and apply algorithms like Dijkstra's, Kruskal's,  Ford's and boruvkato find shortest paths and minimum spanning trees.

## Features

- **Graph Input Methods**:
  - String format (e.g., `A-B:3,B-C:2,C-A:1`)
  - Dictionary format (e.g., `{'A': {'B': 3, 'C': 2}, 'B': {'A': 3, 'C': 1}, 'C': {'A': 2, 'B': 1}}`)

- **Graph Visualization**:
  - Visual representation of the graph using `matplotlib` and `networkx`.

- **Graph Algorithms**:
  - Dijkstra's Algorithm for shortest paths
  - Kruskal's Algorithm for minimum spanning tree
  - Ford's Algorithm for shortest paths

 **Example**

Here is an example of how to use the application:
  - Graph Input as String: A-B:3,B-C:2,C-A:1
  - Graph Input as Dictionary: {'A': {'B': 3, 'C': 2}, 'B': {'A': 3, 'C': 1}, 'C': {'A': 2, 'B': 1}}

**Algorithm Selection**
  - Dijkstra's Algorithm: Finds the shortest paths from a starting vertex.
  - Kruskal's Algorithm: Finds the minimum spanning tree of the graph.
  - Ford's Algorithm: Finds the shortest paths from a starting vertex.

## Contact

For any questions or suggestions, feel free to contact me:
  - Name: Yacine Kermame
  - Email: yacineyoyoker@gmail.com
## Installation

To run this application, you need Python installed on your system along with the required libraries. You can install the required libraries using `pip`:

```sh
pip install matplotlib networkx
  
