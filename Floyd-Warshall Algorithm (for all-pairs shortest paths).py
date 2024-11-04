import networkx as nx
import matplotlib.pyplot as plt

# Define the graph with a negative weight edge
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 6},
    'C': {'D': 3, 'E': 2},
    'D': {'E': 1},
    'E': {}
}

def floyd_warshall(graph):
    nodes = list(graph.keys())
    dist = {i: {j: float('infinity') for j in nodes} for i in nodes}
    path = {i: {j: [] for j in nodes} for i in nodes}
    
    for u in graph:
        dist[u][u] = 0
        path[u][u] = [u]
        for v, weight in graph[u].items():
            dist[u][v] = weight
            path[u][v] = [u, v]
    
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[i][k] + path[k][j][1:]

    return dist, path


# Run Floyd-Warshall algorithm
distances, paths = floyd_warshall(graph)
print("\nFloyd-Warshall Algorithm All-Pairs Shortest Paths:")
for start in distances:
    for end in distances[start]:
        if start != end:
            print(f"From {start} to {end}: Distance = {distances[start][end]}, Path = {paths[start][end]}")

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)

# Define edges to highlight based on shortest paths
highlighted_edges = set()

for start in paths:
    for end in paths[start]:
        if start != end and paths[start][end]:
            for i in range(len(paths[start][end]) - 1):
                highlighted_edges.add((paths[start][end][i], paths[start][end][i + 1]))

# Set the positions of nodes
pos = nx.spring_layout(G, seed=42)  # Random seed for reproducibility

# Draw the graph nodes
node_colors = ['skyblue' if node != 'A' else 'orange' for node in G.nodes()]  # Highlight starting node
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700)

# Draw the edges
edge_color = ['red' if edge in highlighted_edges else 'black' for edge in G.edges()]  # Highlight shortest path edges
nx.draw_networkx_edges(G, pos, edge_color=edge_color, width=2)

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=12, font_color='black', font_weight='bold')

# Set plot title and axis off
plt.title("Graph Visualization with All-Pairs Shortest Paths Highlighted (Floyd-Warshall)", fontsize=15)
plt.axis('off')

# Show the plot
plt.show()
