# pathfinding.py
# this file contains the logic for the A* Search

# imports
import heapq


def heuristic(a, b):
    """
    For this version of A* Search we're using the Manhattan distance.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star_search(start, goal, maze):
    """
    Standard A* Search algorithm.
    Finds a path from start to goal on the maze grid.
    """
    frontier = []
    heapq.heappush(frontier, (0, start))  # pair: (priority, node)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            break  # this means a path has been found

        for neighbor in maze.neighbors(current):
            new_cost = cost_so_far[current] + 1  # all steps have the same cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current

    # reconstruct the path
    path = []
    current = goal
    while current and current in came_from:
        path.append(current)
        current = came_from[current]
    path.reverse()  # from start to goal
    return path
