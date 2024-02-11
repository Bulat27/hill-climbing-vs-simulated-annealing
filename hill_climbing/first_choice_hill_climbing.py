from utilities.common_functions import cycle_length, generate_random_solution, generate_complete_graph, get_random_neighbor
import math

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

def first_choice_hill_climbing_with_restart(graph, max_attempts, num_restarts):
    best_cycle_length = math.inf
    best_solution = None

    for _ in range(num_restarts):
        current_solution, current_cycle_length = first_choice_hill_climbing(graph, max_attempts)

        if current_cycle_length < best_cycle_length:
            best_cycle_length = current_cycle_length
            best_solution = current_solution

    return best_cycle_length, best_solution    
               
