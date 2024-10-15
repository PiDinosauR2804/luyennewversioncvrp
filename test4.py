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

sol = [[[[0, [1]], [7, [7, 10, 8, 6, 9, 4, 3, 5, 2]], [5, []], [3, []], [4, []], [1, []], [2, []], [6, []], [9, []], [8, []], [10, []], [0, []]]], [[[7, [4, 3, 5, 2]]], [[7, [7, 10]]], [[7, [8, 6, 9]]]]]

print(Function.fitness(sol))
# print(Data.manhattan_move_matrix[0][7])
