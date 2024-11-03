
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 6},
    'C': {'D': 3, 'E': -2},
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


distances, paths = floyd_warshall(graph)
print("\nFloyd-Warshall Algorithm All-Pairs Shortest Paths:")
for start in distances:
    for end in distances[start]:
        if start != end:
            print(f"From {start} to {end}: Distance = {distances[start][end]}, Path = {paths[start][end]}")
