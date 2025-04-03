from utils import read_file, display_matrices
from algorithms.ford_fulkerson import ford_fulkerson
from algorithms.min_cost_flow import min_cost_flow

if __name__ == "__main__":
    capacity_matrix, cost_matrix = read_file("graph.txt")
    display_matrices(capacity_matrix, cost_matrix)

    max_flow = ford_fulkerson(capacity_matrix)
    print(f"\nFlot maximal (Ford-Fulkerson) : {max_flow}")

    if cost_matrix is not None:
        min_cost = min_cost_flow(capacity_matrix, cost_matrix)
        print(f"Coût minimal du flot : {min_cost}")
