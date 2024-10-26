import Data
import Function
import Neighborhood
import time
import random
import csv
import Neighborhood11
import Neighborhood10
import Neighborhood_drone
import copy
import numpy as np

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

epsilon = (-1)*0.00001


solution = [[[[0, [1]], [6, [6, 9, 8, 10]], [9, []], [8, []], [10, []], [7, [7, 2, 4, 3]], 
              [0, []], 
              [0, [5]], [2, []], [1, []], [4, []], [3, []], [5, []], 
              [0, []]]], 
            [[[6, [6, 9, 8, 10]]], [[7, [7, 2, 4, 3]]]]]

solution2 = [[[[0, []], [9, [9]]], 
              [[0, []], [10, [10, 3]], [5, [5, 6]], [6, []], [3, []], [4, [4, 1]], [7, [7]], [1, []], [0, []], [8, [8]], [2, [2]]]], 
             [[[9, [9]]], [[10, [10, 3]]], [[5, [5, 6]]], [[4, [4, 1]]], [[7, [7]]], [[8, [8]]], [[2, [2]]]]]

solution3 = [[[[0, []], [3, [3, 9]], [5, [5, 8]], [7, [7, 4]], [9, []], [8, []], [4, []]], [[0, []], [10, [10]], [6, [6]], [1, [1, 2]], [2, []]]], [[[10, [10]]], [[3, [3, 9]]], [[6, [6]]], [[5, [5, 8]]], [[7, [7, 4]]], [[1, [1, 2]]]]]

# print(Function.max_release_date([6]))
# print(Data.manhattan_move_matrix[4][7])
# print(Data.manhattan_move_matrix[10][3])
# print(Data.euclid_flight_matrix[0][5])



# # print(Data.city[10])

# print("-----------------")
print(Function.fitness(solution3)[0])
print(Function.fitness(solution3)[1][0])
print(Function.fitness(solution3)[1][1])


# Nei=Neighborhood10.Neighborhood_one_opt_standard(solution3)
# Nei = Neighborhood.swap_two_array(solution2)
# print(Nei[0][0])
# for i in range(len(Nei)):
#         print("-----------------------", i)
#         print(Nei[i][0][0][0])
#         print(Nei[i][0][0][1])
#         print(Nei[i][0][1])
# print(solution3[0][0])
# print(solution3[0][1])
# print(solution3[1])
# print(Data.number_of_cities)
# print(Data.city)
# print(Data.release_date)

# print(Function.fitness(solution3))