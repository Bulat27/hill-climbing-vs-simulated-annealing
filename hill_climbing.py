from common_functions import cycle_length, generate_random_solution, generate_complete_graph

def get_neighbors(solution):
    neighbors = []

    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = solution.copy()
            neighbor[i] = solution[j]
            neighbor[j] = solution[i]
            neighbors.append(neighbor)

    return neighbors

def get_best_neighbor(graph, neighbors):
    best_cycle_length = cycle_length(graph, neighbors[0])
    best_neighbor = neighbors[0]

    for neighbor in neighbors:
        current_cycle_length = cycle_length(graph, neighbor)

        if current_cycle_length < best_cycle_length:
            best_cycle_length = current_cycle_length
            best_neighbor = neighbor

    return best_neighbor, best_cycle_length

def hill_climbing(graph):
    current_solution = generate_random_solution(graph)
    current_cycle_length = cycle_length(graph, current_solution)
    neighbors = get_neighbors(current_solution)
    best_neighbor, best_neighbor_cycle_length = get_best_neighbor(graph, neighbors)

    while best_neighbor_cycle_length < current_cycle_length:
        current_solution = best_neighbor
        current_cycle_length = best_neighbor_cycle_length
        neighbors = get_neighbors(current_solution)
        best_neighbor, best_neighbor_cycle_length = get_best_neighbor(graph, neighbors)

    return current_solution, current_cycle_length

def main():
    # graph = [
    #     [0, 400, 500, 300],
    #     [400, 0, 300, 500],
    #     [500, 300, 0, 400],
    #     [300, 500, 400, 0]
    # ]

    graph = generate_complete_graph(10)
    for i in range(10):
        print(hill_climbing(graph))

if __name__ == "__main__":
    main()