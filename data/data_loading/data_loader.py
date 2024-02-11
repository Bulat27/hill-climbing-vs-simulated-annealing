import tsplib95
import math
from utilities.common_functions import cycle_length

def load_graph_data_euclidean(filepath):
    problem = tsplib95.load(filepath)
    coordinates = problem.node_coords

    return create_adjacency_matrix_euclidean(coordinates)

def load_graph_data_geo(filepath):
    problem = tsplib95.load(filepath)
    coordinates = problem.node_coords

    return create_adjacency_matrix_geo(coordinates)

def load_graph_data_full_matrix(filepath):
    problem = tsplib95.load(filepath)
    matrix = problem.edge_weights

    return matrix

def create_adjacency_matrix_euclidean(coordinates):
    num_nodes = len(coordinates)
    adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            distance = calculate_distance_euclidean(coordinates[i + 1], coordinates[j + 1])  # Corrected indexing
            adjacency_matrix[i][j] = distance
            adjacency_matrix[j][i] = distance

    return adjacency_matrix

def calculate_distance_euclidean(coord1, coord2):
    xd = coord1[0] - coord2[0]
    yd = coord1[1] - coord2[1]
    distance = math.sqrt(xd * xd + yd * yd)
    rounded_distance = round(distance)  # Round to the nearest integer
    return rounded_distance

def create_adjacency_matrix_geo(coordinates):
    num_nodes = len(coordinates)
    adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            distance = calculate_distance_geo(coordinates[i + 1], coordinates[j + 1])  # Using geo_distance function
            adjacency_matrix[i][j] = distance
            adjacency_matrix[j][i] = distance

    return adjacency_matrix

def calculate_distance_geo(coord1, coord2):
    PI = 3.141592
    RRR = 6378.388
    
    deg_lat1 = int(coord1[0])
    min_lat1 = coord1[0] - deg_lat1
    latitude1 = PI * (deg_lat1 + 5.0 * min_lat1 / 3.0) / 180.0
    
    deg_lon1 = int(coord1[1])
    min_lon1 = coord1[1] - deg_lon1
    longitude1 = PI * (deg_lon1 + 5.0 * min_lon1 / 3.0) / 180.0
    
    deg_lat2 = int(coord2[0])
    min_lat2 = coord2[0] - deg_lat2
    latitude2 = PI * (deg_lat2 + 5.0 * min_lat2 / 3.0) / 180.0
    
    deg_lon2 = int(coord2[1])
    min_lon2 = coord2[1] - deg_lon2
    longitude2 = PI * (deg_lon2 + 5.0 * min_lon2 / 3.0) / 180.0
    
    q1 = math.cos(longitude1 - longitude2)
    q2 = math.cos(latitude1 - latitude2)
    q3 = math.cos(latitude1 + latitude2)
    
    dij = int(RRR * math.acos(0.5 * ((1.0 + q1) * q2 - (1.0 - q1) * q3)) + 1.0)
    
    return dij

def print_adjacency_matrix(adjacency_matrix):
    for row in adjacency_matrix:
        print(" ".join(f"{distance:2d}" for distance in row))

def main():
    # Cannonical tour to test the distance calculation
    adjacency_matrix = load_graph_data_euclidean('data/pcb442.tsp')

    cannonical_tour_length = cycle_length(adjacency_matrix, list(range(len(adjacency_matrix))))
    print(cannonical_tour_length)

    # Check the full matrix loading
    print_adjacency_matrix(load_graph_data_full_matrix('data/bays29.tsp'))

    
if __name__ == "__main__":
    main()
