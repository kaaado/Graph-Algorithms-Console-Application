from collections import defaultdict

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, u, v, weight):
        self.edges[u].append(v)
        self.edges[v].append(u)
        self.weights[(u, v)] = weight
        self.weights[(v, u)] = weight

def boruvka(graph):
    mst = set()
    forest = [{u} for u in graph.edges]
    
    while len(forest) > 1:
        cheapest = defaultdict(lambda: float('inf'))
        for u in graph.edges:
            for v in graph.edges[u]:
                tree1 = next(i for i, tree in enumerate(forest) if u in tree)
                tree2 = next(i for i, tree in enumerate(forest) if v in tree)
                if tree1 != tree2:
                    cost = graph.weights[(u, v)]
                    if cost < cheapest[tree1, tree2]:
                        cheapest[tree1, tree2] = cost
                        cheapest_edge = (u, v)
        
        u, v = cheapest_edge
        tree1 = next(i for i, tree in enumerate(forest) if u in tree)
        tree2 = next(i for i, tree in enumerate(forest) if v in tree)
        mst.add((u, v, graph.weights[(u, v)]))
        
        if len(forest[tree1]) < len(forest[tree2]):
            tree1, tree2 = tree2, tree1
        forest[tree1].update(forest[tree2])
        del forest[tree2]
    
    return mst
# Create a graph with 6 vertices and 9 edges
graph = Graph()
graph.add_edge(0, 1, 4)
graph.add_edge(0, 6, 7)
graph.add_edge(1, 6, 11)
graph.add_edge(1, 7, 20)
graph.add_edge(1, 2, 9)
graph.add_edge(2, 3, 6)
graph.add_edge(2, 4, 2)
graph.add_edge(3, 4, 10)
graph.add_edge(3, 5, 5)
graph.add_edge(4, 5, 15)
graph.add_edge(4, 7, 1)
graph.add_edge(4, 8, 5)
graph.add_edge(5, 8, 12)
graph.add_edge(6, 7, 1)
graph.add_edge(7, 8, 3)

# Find the minimum spanning tree of the graph
mst = boruvka(graph)

# Print the edges in the minimum spanning tree
for u, v, weight in mst:
    print(f"({u}, {v}) - weight: {weight}")

