
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 6},
    'C': {'D': 3, 'E': -2},
    'D': {'E': 1},
    'E': {}
}

def bellman_ford(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    shortest_paths = {node: [] for node in graph}
    shortest_paths[start] = [start]

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    shortest_paths[v] = shortest_paths[u] + [v]

    # Check for negative weight cycles
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] + weight < distances[v]:
                print("Graph contains a negative-weight cycle")
                return None, None

    return distances, shortest_paths


distances, paths = bellman_ford(graph, 'A')
if distances:
    print("\nBellman-Ford Algorithm Shortest Paths from 'A':")
    for node in distances:
        print(f"To {node}: Distance = {distances[node]}, Path = {paths[node]}")
