from collections import defaultdict, deque
import heapq

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



g = Graph()
edges = [
    (1, 2, 4), (1, 3, 2), (2, 3, 5), (2, 4, 10),
    (3, 4, 3), (4, 5, 1), (5, 1, 7)
]

for u, v, w in edges:
    g.add_edge(u, v, w)

# Testing Traversal Schemes
start_node = 1
print("DFS Traversal:", g.dfs(start_node))
print("BFS Traversal:", g.bfs(start_node))

