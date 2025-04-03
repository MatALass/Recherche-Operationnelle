import numpy as np
from collections import deque

def min_cost_flow(capacity_matrix, cost_matrix):
    """Algorithme du flot à coût minimal avec Bellman-Ford."""
    n = len(capacity_matrix)
    source, sink = 0, n - 1

    flow = np.zeros((n, n), dtype=int)
    residual_capacity = np.copy(capacity_matrix)
    residual_cost = np.copy(cost_matrix)

    def bellman_ford():
        """Trouve le plus court chemin en coût avec Bellman-Ford."""
        dist = [float('inf')] * n
        parent = [-1] * n
        queue = deque([source])
        dist[source] = 0

        while queue:
            u = queue.popleft()
            for v in range(n):
                if residual_capacity[u][v] > 0 and dist[u] + residual_cost[u][v] < dist[v]:
                    dist[v] = dist[u] + residual_cost[u][v]
                    parent[v] = u
                    queue.append(v)

        return parent if dist[sink] < float('inf') else None

    total_cost = 0
    while True:
        parent = bellman_ford()
        if not parent:
            break

        min_capacity = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            min_capacity = min(min_capacity, residual_capacity[u][v])
            v = u

        v = sink
        while v != source:
            u = parent[v]
            residual_capacity[u][v] -= min_capacity
            residual_capacity[v][u] += min_capacity
            total_cost += min_capacity * cost_matrix[u][v]
            v = u

    return total_cost
