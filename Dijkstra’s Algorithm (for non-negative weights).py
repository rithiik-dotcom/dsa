import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Define the graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 6},
    'C': {'D': 3, 'E': 5},
    'D': {'E': 1},
    'E': {}
}

# Dijkstra's algorithm implementation
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    shortest_paths = {node: [] for node in graph}
    shortest_paths[start] = [start]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                shortest_paths[neighbor] = shortest_paths[current_node] + [neighbor]

    return distances, shortest_paths

# Run Dijkstra's algorithm from 'A'
distances, paths = dijkstra(graph, 'A')

# Print distances and paths
print("Dijkstra's Algorithm Shortest Paths from 'A':")
for node in distances:
    print(f"To {node}: Distance = {distances[node]}, Path = {paths[node]}")

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)

# Define the shortest paths to highlight
shortest_path_edges = []
for path in paths.values():
    if path:
        for i in range(len(path) - 1):
            shortest_path_edges.append((path[i], path[i + 1]))

# Set the positions of nodes
pos = nx.spring_layout(G, seed=42)  # Random seed for reproducibility

# Draw the graph nodes
node_colors = ['skyblue' if node != 'A' else 'orange' for node in G.nodes()]  # Highlight starting node
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700)

# Draw the edges
edge_color = ['red' if edge in shortest_path_edges else 'black' for edge in G.edges()]  # Highlight shortest path edges
nx.draw_networkx_edges(G, pos, edge_color=edge_color, width=2)

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=12, font_color='black', font_weight='bold')

# Set plot title and axis off
plt.title("Graph Visualization with Shortest Paths Highlighted", fontsize=15)
plt.axis('off')

# Show the plot
plt.show()
