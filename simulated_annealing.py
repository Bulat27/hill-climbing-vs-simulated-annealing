import random
import math
from common_functions import cycle_length, generate_random_solution, generate_complete_graph

def simulated_annealing(graph, initial_temperature, cooling_rate):
    current_solution = generate_random_solution(graph)
    current_cycle_length = cycle_length(graph, current_solution)
    current_temperature = initial_temperature
    
    while current_temperature > 1e-5:
        random_neighbor = get_random_neighbor(current_solution)
        random_neighbor_length = cycle_length(graph, random_neighbor)
        
        delta = random_neighbor_length - current_cycle_length
        
        if delta < 0 or random.random() <= math.exp(-delta / current_temperature): 
            current_solution = random_neighbor
            current_cycle_length = random_neighbor_length
        
        current_temperature *= cooling_rate
    
    return current_solution, current_cycle_length

def get_random_neighbor(solution):
    random_neighbor = solution.copy()
    i, j = random.sample(range(len(solution)), 2)
    random_neighbor[i], random_neighbor[j] = random_neighbor[j], random_neighbor[i]

    return random_neighbor

def main():
    graph = generate_complete_graph(10)
    initial_temperature = 1000
    cooling_rate = 0.99
    
    for _ in range(10):
        print(simulated_annealing(graph, initial_temperature, cooling_rate))

if __name__ == "__main__":
    main()

