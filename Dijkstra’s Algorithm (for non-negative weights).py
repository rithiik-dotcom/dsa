import heapq


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 6},
    'C': {'D': 3, 'E': 5},
    'D': {'E': 1},
    'E': {}
}

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


distances, paths = dijkstra(graph, 'A')
print("Dijkstra's Algorithm Shortest Paths from 'A':")
for node in distances:
    print(f"To {node}: Distance = {distances[node]}, Path = {paths[node]}")
