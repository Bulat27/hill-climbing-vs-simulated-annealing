import random
import math
from utilities.common_functions import cycle_length, generate_random_solution, get_random_neighbor

def simulated_annealing(graph, initial_temperature, cooling_rate, max_iterations, end_temperature=1):
    current_solution = generate_random_solution(graph)
    current_cycle_length = cycle_length(graph, current_solution)
    current_temperature = initial_temperature

    best_solution = current_solution
    best_cycle_length = current_cycle_length

    scores = [] 
    scores.append(current_cycle_length)

    counter = 0
    
    while current_temperature >= end_temperature and counter < max_iterations:
        random_neighbor = get_random_neighbor(current_solution)
        random_neighbor_length = cycle_length(graph, random_neighbor)
        
        delta = random_neighbor_length - current_cycle_length
        
        if delta < 0 or random.random() <= math.exp(-delta / current_temperature): 
            current_solution = random_neighbor
            current_cycle_length = random_neighbor_length
        
        if current_cycle_length < best_cycle_length:
            best_cycle_length = current_cycle_length
            best_solution = current_solution
        
        current_temperature *= cooling_rate
        scores.append(current_cycle_length)

        counter += 1

    return best_solution, best_cycle_length, scores

def calculate_initial_temperature(graph, num_samples=1000, coefficient=0.9):
    total_neighbor_difference = 0.0

    initial_solution = generate_random_solution(graph)
    initial_length = cycle_length(graph, initial_solution)

    for _ in range(num_samples):
        neighbor = get_random_neighbor(initial_solution)
        neighbor_length = cycle_length(graph, neighbor)
        total_neighbor_difference += abs(neighbor_length - initial_length)

    average_initial_neighbor_difference = total_neighbor_difference / num_samples
    initial_temperature = coefficient * average_initial_neighbor_difference  

    return initial_temperature
