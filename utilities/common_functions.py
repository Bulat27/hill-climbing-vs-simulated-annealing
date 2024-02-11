import random

def generate_random_solution(graph):
    cities = list(range(len(graph)))
    solution = []

    for _ in range(len(graph)):
        random_city = cities[random.randint(0, len(cities) - 1)]
        solution.append(random_city)
        cities.remove(random_city)

    return solution

def cycle_length(tsp, solution):
    cycle_length = 0

    for i in range(len(solution)):
        cycle_length += tsp[solution[i - 1]][solution[i]]

    return cycle_length

def generate_complete_graph(number_of_nodes):
    graph = []

    for i in range(number_of_nodes):
        distances = []
        for j in range(number_of_nodes):
            if j == i:
                distances.append(0)
            elif j < i:
                distances.append(graph[j][i])
            else:
                distances.append(random.randint(10, 1000))
        graph.append(distances)
        
    return graph

def get_random_neighbor(solution):
    random_neighbor = solution.copy()
    i, j = random.sample(range(len(solution)), 2)
    random_neighbor[i], random_neighbor[j] = random_neighbor[j], random_neighbor[i]

    return random_neighbor