# ############################################################################################################# #
# Outside source : A* (A Star) Search Algorithm - Computerphile : [https://www.youtube.com/watch?v=ySN5Wnu88nE] #
# ############################################################################################################# #
import math
from heapq import heappush, heappop

def heuristic_euclidean_distance(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))


def shortest_path_building(came_from, start, goal):

    if not came_from:
        return []

    shortest_path = [goal]

    current = goal

    while current != start:
        current = came_from[current]
        shortest_path.append(current)

    shortest_path.reverse()
    return shortest_path


def shortest_path(M,start,goal):
    print("shortest path called")
    
    open_set = []
    closed_set = set()
    came_from = {}
    total_cost = {}
    
    heappush(open_set, 
             (heuristic_euclidean_distance(
                 M.intersections[start],
                 M.intersections[goal]), start))

    came_from[start] = None
    total_cost[start] = 0
    
    while open_set:
        _, current = heappop(open_set)
        
        if current ==  goal:
            return shortest_path_building(came_from, start, goal)
        
        closed_set.add(current)
        
        for intersection in M.roads[current]:
            if intersection in closed_set:
                continue
            
            g_cost = total_cost[current] + \
                   heuristic_euclidean_distance(M.intersections[current],
                                                M.intersections[intersection])
            
            if intersection not in total_cost or g_cost < total_cost[intersection]:
                total_cost[intersection] = g_cost
                h_cost = g_cost + heuristic_euclidean_distance(M.intersections[intersection],
                                                M.intersections[goal])
                heappush(open_set, (h_cost, intersection))
                came_from[intersection] = current
    return shortest_path_building({}, start, goal)