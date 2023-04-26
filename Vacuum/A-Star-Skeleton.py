# import heapq
#
# # Function to calculate the heuristic cost from the current cell to the nearest dirt cell
# def heuristic_cost(current_cell, dirt_cells):
#     # Replace this with your own heuristic function
#     return 0
#
# # Function to calculate the movement cost from the current cell to the next cell
# def movement_cost(current_cell, next_cell):
#     # Replace this with your own movement cost function
#     return 0
#
# # Function to get the neighboring cells of the current cell
# def get_neighbors(current_cell, width, height):
#     neighbors = []
#     # Add the neighboring cells to the neighbors list
#     return neighbors
#
# def a_star_algorithm(world, agent_pos, width, height):
#     # Create an open list and a closed list
#     open_list = []
#     closed_list = set()
#     # Find the dirt cells in the grid
#     dirt_cells = []
#     # Add the agent's starting position to the open list
#     heapq.heappush(open_list, (0, agent_pos))
#     # While the open list is not empty
#     while open_list:
#         # Get the cell with the lowest total cost from the open list
#         current_cost, current_cell = heapq.heappop(open_list)
#         # Add the current cell to the closed list
#         closed_list.add(current_cell)
#         # If the current cell is a dirt cell
#         if current_cell in dirt_cells:
#             dirt_cells.remove(current_cell)
#             # If all the dirt cells have been cleaned, return the closed list (i.e. the path taken by the agent)
#             if not dirt_cells:
#                 return closed_list
#         # Get the neighboring cells of the current cell
#         for next_cell in get_neighbors(current_cell, width, height):
#             # If the next cell is not in the closed list
#             if next_cell not in closed_list:
#                 # Calculate the movement cost
#                 move_cost = movement_cost(current_cell, next_cell)
#                 # Calculate the total cost (heuristic cost + movement cost)
#                 total_cost = heuristic_cost(next_cell, dirt_cells) + move_cost
#                 # Add the next cell to the open list
#                 heapq.heappush(open_list, (total_cost, next_cell))
#     return closed_list

"""Distance Measuring Functions"""
# def manhattan_distance(current_cell, dirt_cells):
#     closest_dirt_distance = float('inf')
#     for dirt_cell in dirt_cells:
#         x1, y1 = current_cell
#         x2, y2 = dirt_cell
#         distance = abs(x1 - x2) + abs(y1 - y2)
#         if distance < closest_dirt_distance:
#             closest_dirt_distance = distance
#     return closest_dirt_distance


# import math
#
# def euclidean_distance(current_cell, dirt_cells):
#     closest_dirt_distance = float('inf')
#     for dirt_cell in dirt_cells:
#         x1, y1 = current_cell
#         x2, y2 = dirt_cell
#         distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
#         if distance < closest_dirt_distance:
#             closest_dirt_distance = distance
#     return closest_dirt_distance