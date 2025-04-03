import numpy as np

def read_file(file_path):
    """Lecture des matrices de capacité et de coût depuis un fichier."""
    with open(file_path, 'r') as file:
        blocks = file.read().strip().split("\n\n")

    matrices = [np.array([list(map(int, line.split())) for line in block.split("\n")]) for block in blocks]

    if len(matrices) < 1:
        raise ValueError("Le fichier doit contenir au moins une matrice de capacité.")

    capacity_matrix = matrices[0]
    cost_matrix = matrices[1] if len(matrices) > 1 else None

    return capacity_matrix, cost_matrix

def display_matrices(capacity_matrix, cost_matrix=None):
    """Affiche proprement les matrices."""
    def print_matrix(matrix, title):
        print(f"\n{title}:")
        for row in matrix:
            print(" ".join(f"{val:3}" for val in row))

    print_matrix(capacity_matrix, "Matrice des capacités")
    if cost_matrix is not None:
        print_matrix(cost_matrix, "Matrice des coûts")
