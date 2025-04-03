import numpy as np
from collections import deque

def find_augmenting_path(residual_graph, source, sink, parent):
    """Recherche d'un chemin augmentant avec BFS."""
    n = len(residual_graph)
    visited = [False] * n
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()
        for v, capacity in enumerate(residual_graph[u]):
            if capacity > 0 and not visited[v]:
                parent[v] = u
                visited[v] = True
                queue.append(v)
                if v == sink:
                    return True
    return False

def ford_fulkerson(capacity_matrix):
    """Implémentation de l'algorithme Ford-Fulkerson."""
    source, sink = 0, len(capacity_matrix) - 1
    residual_graph = np.copy(capacity_matrix)
    parent = [-1] * len(capacity_matrix)
    max_flow = 0

    while find_augmenting_path(residual_graph, source, sink, parent):
        path_flow = float('Inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual_graph[u][v])
            v = u

        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = u

        max_flow += path_flow

    return max_flow
