import Data
import Function
import Neighborhood
import time
import random
import csv
import Neighborhood11
import Neighborhood10
import Neighborhood_drone

global LOOP
global tabu_tenure
# global best_sol
# global best_fitness
global Tabu_Structure
global current_neighborhood
global LOOP_IMPROVED
global SET_LAST_10
global BEST
global start_time
global Data1

solution = [[[[0, [1]], [4, [4, 5, 15]], [5, []], [3, []], [1, []], [2, [2, 11, 10, 13, 14]], [7, []], [6, []], [8, []], [12, [12, 9]], [10, []], [11, []], [9, []], [13, []], [15, []], [14, []]]], 
            [[[4, [4, 5]]], [[2, [2, 11, 13]]], [[2, [10, 14]]], [[12, [12, 9, 15]]]]]
l = 1
change = [15]

# new = Neighborhood.groupTripInDroneRoute(solution, change, 0, l)
# print(new)
solution = Function.initial_solution7()
# solution = [[[[0, [1]], [4, [4, 5, 15]], [5, []], [3, []], [1, []], [2, [2, 11, 10, 13, 14]], [7, []], [6, []], [8, []], [12, [12, 9]], [10, []], [11, []], [9, []], [13, []], [15, []], [14, []], [0, []]]], 
#             [[[4, [4, 5, 15]]], [[2, [2, 11, 13]]], [[2, [10, 14]]], [[12, [12, 9, 15]]]]]
print(solution)
# sol = Neighborhood.updateDroneQueueReturnNewIndex(solution, 0)
sol = Neighborhood.Turn_single_to_k_trip(solution, 4)
print(sol)