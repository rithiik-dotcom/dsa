
import heapq


edges = [
    ('A', 'B', 1), ('A', 'C', 4),
    ('B', 'C', 2), ('B', 'D', 5),
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
            mst.append((weight, v))
            for next_edge in adj_list[v]:
                if next_edge[1] not in visited:
                    heapq.heappush(min_edges, next_edge)

    return mst


print("Kruskal's MST:", kruskal_mst(vertices, edges))
print("Prim's MST:", prim_mst(vertices, edges))
