from queue import PriorityQueue

# Define the graph as a dictionary of dictionaries
graph = {'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
         'Zerind': {'Arad': 75, 'Oradea': 71},
         'Oradea': {'Zerind': 71, 'Sibiu': 151},
         'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
         'Timisoara': {'Arad': 118, 'Lugoj': 111},
         'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
         'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
         'Drobeta': {'Mehadia': 75, 'Craiova': 120},
         'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
         'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
         'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
         'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
         'Bucharest': {'Fagaras': 211, 'Pitesti': 101}}

def uniform_cost_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    explored = []
    path = {}
    path[start] = None

    while not frontier.empty():
        cost, current_node = frontier.get()
        explored.append(current_node)

        if current_node == goal:
            final_path = []
            while current_node in path:
                final_path.append(current_node)
                current_node = path[current_node]
            final_path.reverse()
            return final_path

        for neighbor, neighbor_cost in graph[current_node].items():
            if neighbor not in explored:
                new_cost = cost + neighbor_cost
                if neighbor not in [node[1] for node in frontier.queue]:
                    frontier.put((new_cost, neighbor))
                    path[neighbor] = current_node
                elif new_cost < [node[0] for node in frontier.queue if node[1] == neighbor][0]:
                    frontier.get([node for node in frontier.queue if node[1] == neighbor][0])
                    frontier.put((new_cost, neighbor))
                    path[neighbor] = current_node

    return None

# Test the uniform cost search algorithm
start_node = 'Arad'
goal_node = 'Bucharest'
result_path = uniform_cost_search(graph, start_node, goal_node)

if result_path:
    print("The minimum distance path from", start_node, "to", goal_node, "is:")
    print(result_path)
    print("The total distance is:", sum(graph[result_path[i]][result_path[i+1]] for i in range(len(result_path)-1)))
else:
    print("Goal not reachable from the starting node")
