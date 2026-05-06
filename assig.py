
from collections import deque

graph = {
    'A': ['C', 'B', 'D'],
    'B': ['A', 'C', 'E', 'G'],
    'C': ['A', 'B', 'D'],
    'D': ['C', 'A'],
    'E': ['G', 'F', 'B'],
    'F': ['G', 'E'],
    'G': ['F', 'B']
}


def dfs(graph, start):
    visited = set()
    result = []

    def dfs_visit(node):
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                dfs_visit(neighbor)

    dfs_visit(start)
    return result



def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result




print("DFS:", " -> ".join(dfs(graph, 'A')))
print("BFS:", " -> ".join(bfs(graph, 'A')))



# TASK 4: Dijkstra


import heapq

road_graph = {
    'Edinburgh': [('Stirling', 50), ('Glasgow', 70), ('Perth', 100)],
    'Stirling': [('Edinburgh', 50), ('Perth', 40), ('Glasgow', 50)],
    'Glasgow': [('Edinburgh', 70), ('Stirling', 50)],
    'Perth': [('Edinburgh', 100), ('Stirling', 40), ('Dundee', 60)],
    'Dundee': [('Perth', 60)]
}


def dijkstra(graph, start, end):
    pq = [(0, start)]  # (distance, node)
    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}

    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node == end:
            break

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))


    path = []
    node = end
    while node:
        path.append(node)
        node = previous[node]

    path.reverse()

    return path, distances[end]



path, distance = dijkstra(road_graph, 'Edinburgh', 'Dundee')

print("\nShortest Path:", " -> ".join(path))
print("Total Distance:", distance)
