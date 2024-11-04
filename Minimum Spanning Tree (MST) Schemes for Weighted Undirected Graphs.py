import heapq
import matplotlib.pyplot as plt
import networkx as nx

edges = [
    ('A', 'B', 1), ('A', 'C', 4),
    ('B', 'C', 5), ('B', 'D', 5),
    ('C', 'D', 3)
]

vertices = ['A', 'B', 'C', 'D']

class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
    
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])  # Path compression
        return self.parent[v]
    
    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 != root2:
            self.parent[root1] = root2

# Kruskal's Algorithm
def kruskal_mst(vertices, edges):
    uf = UnionFind(vertices)
    mst = []
    edges_sorted = sorted(edges, key=lambda x: x[2])  # Sort edges by weight

    for v1, v2, weight in edges_sorted:
        if uf.find(v1) != uf.find(v2):
            uf.union(v1, v2)
            mst.append((v1, v2, weight))

    return mst

# Prim's Algorithm
def prim_mst(vertices, edges):
    adj_list = {v: [] for v in vertices}
    for v1, v2, weight in edges:
        adj_list[v1].append((weight, v2))
        adj_list[v2].append((weight, v1))

    start_vertex = vertices[0]
    mst = []
    visited = set([start_vertex])
    min_edges = adj_list[start_vertex]
    heapq.heapify(min_edges)

    while min_edges:
        weight, v = heapq.heappop(min_edges)
        if v not in visited:
            visited.add(v)
            mst.append((start_vertex, v, weight))  # Include the edge to the MST
            for next_edge in adj_list[v]:
                if next_edge[1] not in visited:
                    heapq.heappush(min_edges, next_edge)
            start_vertex = v  # Update start vertex for the next iteration

    return mst

# Find MSTs
kruskal_mst_result = kruskal_mst(vertices, edges)
prim_mst_result = prim_mst(vertices, edges)

# Print results
print("Kruskal's MST:", kruskal_mst_result)
print("Prim's MST:", prim_mst_result)


# Visualization for Kruskal's MST
G_kruskal = nx.Graph()
for v1, v2, weight in edges:
    G_kruskal.add_edge(v1, v2, weight=weight)

# Draw Kruskal's MST
G_kruskal_mst = nx.Graph()
for v1, v2, weight in kruskal_mst_result:
    G_kruskal_mst.add_edge(v1, v2, weight=weight)

pos_kruskal = nx.spring_layout(G_kruskal, seed=42)
plt.figure(figsize=(8, 5))
nx.draw_networkx_nodes(G_kruskal_mst, pos_kruskal, node_color='skyblue', node_size=700)
nx.draw_networkx_edges(G_kruskal_mst, pos_kruskal, width=2, edge_color='red')
nx.draw_networkx_labels(G_kruskal_mst, pos_kruskal, font_size=12, font_color='black', font_weight='bold')
edge_labels_kruskal = nx.get_edge_attributes(G_kruskal_mst, 'weight')
nx.draw_networkx_edge_labels(G_kruskal_mst, pos_kruskal, edge_labels=edge_labels_kruskal)
plt.title("Kruskal's MST")
plt.axis('off')
plt.show()

# Visualization for Prim's MST
G_prim = nx.Graph()
for v1, v2, weight in edges:
    G_prim.add_edge(v1, v2, weight=weight)

# Draw Prim's MST
G_prim_mst = nx.Graph()
for v1, v2, weight in prim_mst_result:
    G_prim_mst.add_edge(v1, v2, weight=weight)

pos_prim = nx.spring_layout(G_prim, seed=42)
plt.figure(figsize=(8, 5))
nx.draw_networkx_nodes(G_prim_mst, pos_prim, node_color='lightgreen', node_size=700)
nx.draw_networkx_edges(G_prim_mst, pos_prim, width=2, edge_color='blue')
nx.draw_networkx_labels(G_prim_mst, pos_prim, font_size=12, font_color='black', font_weight='bold')
edge_labels_prim = nx.get_edge_attributes(G_prim_mst, 'weight')
nx.draw_networkx_edge_labels(G_prim_mst, pos_prim, edge_labels=edge_labels_prim)
plt.title("Prim's MST")
plt.axis('off')
plt.show()
