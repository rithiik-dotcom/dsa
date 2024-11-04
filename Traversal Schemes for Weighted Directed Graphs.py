from collections import defaultdict, deque
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, weight=1):
        self.graph[u].append((v, weight))

    def dfs(self, start):
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor, _ in reversed(self.graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor, _ in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result

# Separate Graphs for DFS and BFS
g_dfs = Graph()
g_bfs = Graph()

# Add edges to both graphs
edges = [
    (1, 2, 4), (1, 3, 2), (2, 3, 5), (2, 4, 10),
    (3, 4, 3), (4, 5, 1), (5, 1, 7)
]

for u, v, w in edges:
    g_dfs.add_edge(u, v, w)
    g_bfs.add_edge(u, v, w)

# Testing Traversal Schemes
start_node = 1
print("DFS Traversal:", g_dfs.dfs(start_node))
print("BFS Traversal:", g_bfs.bfs(start_node))

# Visualization for DFS
G_dfs = nx.DiGraph()
for u, v, w in edges:
    G_dfs.add_edge(u, v, weight=w)

# Draw the DFS graph
pos_dfs = nx.spring_layout(G_dfs, seed=42)
plt.figure(figsize=(8, 5))
nx.draw_networkx_nodes(G_dfs, pos_dfs, node_color='skyblue', node_size=700)
nx.draw_networkx_edges(G_dfs, pos_dfs, width=2, alpha=0.5, edge_color='black')
nx.draw_networkx_labels(G_dfs, pos_dfs, font_size=12, font_color='black', font_weight='bold')
edge_labels_dfs = nx.get_edge_attributes(G_dfs, 'weight')
nx.draw_networkx_edge_labels(G_dfs, pos_dfs, edge_labels=edge_labels_dfs)
plt.title("Graph for DFS Traversal")
plt.axis('off')
plt.show()

# Visualization for BFS
G_bfs = nx.DiGraph()
for u, v, w in edges:
    G_bfs.add_edge(u, v, weight=w)

# Draw the BFS graph
pos_bfs = nx.spring_layout(G_bfs, seed=42)
plt.figure(figsize=(8, 5))
nx.draw_networkx_nodes(G_bfs, pos_bfs, node_color='lightgreen', node_size=700)
nx.draw_networkx_edges(G_bfs, pos_bfs, width=2, alpha=0.5, edge_color='black')
nx.draw_networkx_labels(G_bfs, pos_bfs, font_size=12, font_color='black', font_weight='bold')
edge_labels_bfs = nx.get_edge_attributes(G_bfs, 'weight')
nx.draw_networkx_edge_labels(G_bfs, pos_bfs, edge_labels=edge_labels_bfs)
plt.title("Graph for BFS Traversal")
plt.axis('off')
plt.show()
