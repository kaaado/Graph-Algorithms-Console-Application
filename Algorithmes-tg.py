import networkx as nx
import matplotlib.pyplot as plt
import heapq
import ast

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def kruskal(graph):
    mst = []
    edges = [(graph[u][v], u, v) for u in graph for v in graph[u]]
    edges.sort()

    parent = {node: node for node in graph}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        parent[root_u] = root_v

    for edge in edges:
        weight, u, v = edge
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))

    return mst

def ford(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    return distances



def display_graph(graph, display_edge_weights=False):
    G = nx.Graph()
    for u, neighbors in graph.items():
        for v, weight in neighbors.items():
            G.add_edge(u, v, weight=weight)

    pos = nx.spring_layout(G) 
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8, font_color="black", font_weight="bold", edge_color="gray", linewidths=0.5, connectionstyle='arc3,rad=0.1')
    
    if display_edge_weights:
        edge_labels = {(u, v): G[u][v]['weight'] for (u, v) in G.edges()}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()

def convert_to_dict(input_str):
    result_dict = {}
    for item in input_str.split(','):
        nodes, weight = item.split(':')
        node_a, node_b = nodes.split('-')
        weight = int(weight)
        
        if node_a not in result_dict:
            result_dict[node_a] = {}
        if node_b not in result_dict:
            result_dict[node_b] = {}
            
        result_dict[node_a][node_b] = weight
        result_dict[node_b][node_a] = weight

    return result_dict



def main():
    example_graph = {'A': {'B': 3, 'C': 2}, 'B': {'A': 3, 'C': 1}, 'C': {'A': 2, 'B': 1}}
    example_graph2 = "A-B:3,B-C:2,C-A:1"
    print("Graph Menu:")
    print(f"1. Enter the graph as a string (e.g., {example_graph2}") or str(example_graph2)
    print(f"2. Enter the graph as a dictionary (e.g., {example_graph})") or str(example_graph)
    printer_choice = input("Enter the number of the graph how you want to enter: ")

    if printer_choice == '1':
        input_str = input("Enter the graph as a string (e.g., A-B:3,B-C:2,C-A:1): ")
        user_graph = convert_to_dict(input_str)
    elif printer_choice == '2':
        
         user_graph_input = input(f"Enter the graph as a dictionary (e.g., {example_graph}): ") or str(example_graph)
         try:
          user_graph = ast.literal_eval(user_graph_input)
         except (ValueError, SyntaxError):
           print("Error: Invalid dictionary format. Please provide a valid dictionary.")
           return
    else:
        print("Invalid choice.")
        return
    
    print("\nUser-Provided Graph:")
    display_graph(user_graph, display_edge_weights=True)
    print("\nAlgorithm Menu:")
    print("1. Dijkstra's Algorithm")
    print("2. Kruskal's Algorithm")
    print("3. Ford's Algorithm")

    algorithm_choice = input("Enter the number of the algorithm you want to apply: ")

    if algorithm_choice == "1":
        start_vertex = input("Enter the start vertex for Dijkstra's Algorithm: ").upper()
        distances_from_start = dijkstra(user_graph, start_vertex)
        print("\nShortest Paths from", start_vertex, ":")
        for vertex, distance in distances_from_start.items():
            if distance != float('infinity') and vertex != start_vertex:
                path = nx.shortest_path(nx.Graph(user_graph), source=start_vertex, target=vertex)
                path_string = " -> ".join(path)
                print(f"To {vertex}: Distance: {distance}, Path: {path_string}")

    elif algorithm_choice == "2":
        mst_edges = kruskal(user_graph)
        print("\nMinimum Spanning Tree (Kruskal's Algorithm):")
        print("Edge List:")
        for edge in mst_edges:
            u, v, weight = edge
            print(f"Edge: {u} - {v}, Weight: {weight}")

    elif algorithm_choice == "3":
        start_vertex = input("Enter the start vertex for Ford's Algorithm: ").upper()
        distances_from_start = ford(user_graph, start_vertex)
        print("\nShortest Distances from", start_vertex, ":")
        for vertex, distance in distances_from_start.items():
            if distance != float('infinity') and vertex != start_vertex:
                print(f"To {vertex}: Distance: {distance}")
    else:
        print("Invalid algorithm choice.")

if __name__ == "__main__":
    main()
