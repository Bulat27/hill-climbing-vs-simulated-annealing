import tsplib95
import math
from common_functions import cycle_length

def calculate_distance(coord1, coord2):
    xd = coord1[0] - coord2[0]
    yd = coord1[1] - coord2[1]
    distance = math.sqrt(xd * xd + yd * yd)
    rounded_distance = round(distance)  # Round to the nearest integer
    return rounded_distance

def create_adjacency_matrix(coordinates):
    num_nodes = len(coordinates)
    adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            distance = calculate_distance(coordinates[i + 1], coordinates[j + 1])  # Corrected indexing
            adjacency_matrix[i][j] = distance
            adjacency_matrix[j][i] = distance

    return adjacency_matrix

def print_adjacency_matrix(adjacency_matrix):
    for row in adjacency_matrix:
        print(" ".join(f"{distance:2d}" for distance in row))

problem = tsplib95.load('data/pcb442.tsp')

coordinates = problem.node_coords

adjacency_matrix = create_adjacency_matrix(coordinates)

cannonical_tour_length = cycle_length(adjacency_matrix, list(range(len(adjacency_matrix))))
print(cannonical_tour_length)


