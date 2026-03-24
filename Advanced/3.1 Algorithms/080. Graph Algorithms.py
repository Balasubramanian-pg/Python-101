import heapq
from collections import defaultdict, deque

# -------------------------------
# 1. Dijkstra's Algorithm
# -------------------------------
def dijkstra(graph, start):
    """
    graph: dict {node: [(neighbor, weight)]}
    start: starting node
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        current_dist, node = heapq.heappop(pq)

        if current_dist > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# -------------------------------
# 2. Bellman-Ford Algorithm
# -------------------------------
def bellman_ford(edges, vertices, start):
    """
    edges: list of (u, v, weight)
    vertices: number of vertices
    start: source node
    """
    dist = [float('inf')] * vertices
    dist[start] = 0

    # Relax edges V-1 times
    for _ in range(vertices - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Detect negative cycle
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            raise ValueError("Graph contains negative weight cycle")

    return dist


# -------------------------------
# 3. Floyd-Warshall Algorithm
# -------------------------------
def floyd_warshall(matrix):
    """
    matrix: adjacency matrix
    """
    n = len(matrix)
    dist = [row[:] for row in matrix]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j])
    return dist


# -------------------------------
# 4. Topological Sort (Kahn’s Algorithm)
# -------------------------------
def topological_sort(graph):
    """
    graph: dict {node: [neighbors]}
    """
    indegree = {node: 0 for node in graph}

    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = deque([node for node in graph if indegree[node] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) != len(graph):
        raise ValueError("Graph has a cycle")

    return topo_order


# -------------------------------
# 5. Union-Find (Disjoint Set)
# -------------------------------
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


# -------------------------------
# 6. Kruskal’s Algorithm (MST)
# -------------------------------
def kruskal(n, edges):
    """
    n: number of nodes
    edges: list of (u, v, weight)
    """
    uf = UnionFind(n)
    edges.sort(key=lambda x: x[2])

    mst = []
    total_weight = 0

    for u, v, w in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, w))
            total_weight += w

    return mst, total_weight


# -------------------------------
# 7. Prim’s Algorithm (MST)
# -------------------------------
def prim(graph, start):
    """
    graph: dict {node: [(neighbor, weight)]}
    """
    visited = set()
    min_heap = [(0, start)]
    total_weight = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        total_weight += weight

        for neighbor, w in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor))

    return total_weight


# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }

    print("Dijkstra:", dijkstra(graph, 0))

    edges = [
        (0, 1, 4),
        (0, 2, 1),
        (2, 1, 2),
        (1, 3, 1),
        (2, 3, 5)
    ]

    print("Bellman-Ford:", bellman_ford(edges, 4, 0))

    matrix = [
        [0, 3, float('inf')],
        [2, 0, float('inf')],
        [float('inf'), 7, 0]
    ]

    print("Floyd-Warshall:", floyd_warshall(matrix))

    dag = {
        5: [2, 0],
        4: [0, 1],
        2: [3],
        3: [1],
        1: [],
        0: []
    }

    print("Topological Sort:", topological_sort(dag))

    print("Kruskal:", kruskal(4, edges))
    print("Prim:", prim(graph, 0))
