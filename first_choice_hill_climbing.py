import data_loader
from common_functions import cycle_length, generate_random_solution, generate_complete_graph, get_random_neighbor

def first_choice_hill_climbing(graph, max_attempts=1000):
    current_solution = generate_random_solution(graph)
    current_cycle_length = cycle_length(graph, current_solution)

    while True:
        improved = False
        for _ in range(max_attempts):
            neighbor = get_random_neighbor(current_solution)
            neighbor_cycle_length = cycle_length(graph, neighbor)

            if neighbor_cycle_length < current_cycle_length:
                current_solution = neighbor
                current_cycle_length = neighbor_cycle_length
                improved = True
                break  # Stop if better neighbor found

        if not improved:
            break  # Stop if no better neighbor found

    return current_solution, current_cycle_length

def main():
    # Load your TSPLIB instance here
    # graph = ...

    # for i in range(10):
    #     start_time = time.time()
    #     cycle, cycle_length = first_choice_hill_climbing(graph)
    #     print(time.time() - start_time)

    graph = data_loader.adjacency_matrix
    cycle, cycle_length = first_choice_hill_climbing(graph)

    print(cycle_length)

if __name__ == "__main__":
    main()
