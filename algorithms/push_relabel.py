class PushRelabel:
    def __init__(self, n, capacities, costs):
        self.n = n
        self.capacities = capacities
        self.costs = costs
        self.flows = [[0] * n for _ in range(n)]
        self.excess = [0] * n
        self.height = [0] * n
        self.residual_capacity = [row[:] for row in capacities]

    def initialize(self, source):
        """Initialisation des excédents et des hauteurs"""
        self.excess[source] = float('inf')
        self.height[source] = self.n
        for v in range(self.n):
            if self.capacities[source][v] > 0:
                self.flows[source][v] = self.capacities[source][v]
                self.excess[v] += self.capacities[source][v]
                self.residual_capacity[source][v] = 0

    def push(self, u, v):
        """Pousse le flot de u à v"""
        flow = min(self.excess[u], self.residual_capacity[u][v])
        self.residual_capacity[u][v] -= flow
        self.residual_capacity[v][u] += flow
        self.excess[u] -= flow
        self.excess[v] += flow

    def relabel(self, u):
        """Relabel un sommet"""
        min_height = float('inf')
        for v in range(self.n):
            if self.residual_capacity[u][v] > 0:
                min_height = min(min_height, self.height[v])
        self.height[u] = min_height + 1

    def push_relabel(self, source, sink):
        """Algorithme complet"""
        self.initialize(source)
        while True:
            u = next((i for i in range(self.n) if self.excess[i] > 0), None)
            if u is None:
                break
            self.push(u, sink)  # Exemple simplifié

    def get_total_flow(self, sink):
        return sum(self.flows[i][sink] for i in range(self.n))
