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


solution = [[[[0, [1]], [11, [15, 14, 5, 11, 3, 7, 10, 9, 12, 4, 6, 8]], [7, [2, 13]], [8, []], [4, []], [5, []], [3, []], [1, []], [2, []], [6, []], [10, []], [9, []], [13, []], [15, []], [14, []], [12, []], [0, []]]], [[[11, [11]]], [[11, [5, 3, 4]]], [[11, [15, 14, 7, 10]]], [[11, [9, 12, 6, 8]]], [[7, [2, 13]]]]]

new_ = [[[[0, [1]], [1, []], [2, [12, 2, 11, 3, 5, 4, 13, 14, 10]], [3, []], [5, []], [4, []], [10, []], [9, [9, 15]], [13, []], [15, []], [11, []], [14, []], [12, []], [0, []], [6, [6, 7, 8]], [7, []], [8, []]]], [[[2, [11, 13]]], [[2, [2, 3, 5, 4]]], [[2, [12, 14, 10]]], [[9, [9, 15]]], [[6, [6, 7, 8]]]]]

print(Data.number_of_cities)

a = np.arange(1, Data.number_of_cities)
print(a)

# print(new_[0][0])

# print(Function.fitness(new_))
# j = 0
# sol = copy.deepcopy(new_)
# print(sol)
# sol = [sol]
# aa = sol
# min_to_improve = Function.fitness(new_)[0]
# # list_neighborhood = [Neighborhood_drone.Neighborghood_change_drone_route_max_pro_plus_for_specific_truck, Neighborhood_drone.Neighborhood_group_trip]
# # list_neighborhood = [Neighborhood_drone.Neighborghood_change_drone_route_max_pro_plus_for_specific_truck, Neighborhood_drone.Neighborhood_change_index_trip, Neighborhood_drone.Neighborhood_group_trip]       
# list_neighborhood = [Neighborhood_drone.Neighborghood_change_drone_route_max_pro_plus, Neighborhood_drone.Neighborhood_change_index_trip]       
# while j < 2:
#         j += 1
#         # print("i: ",i," j: ", j)
#         # print(sol[0])
#         for k in range(len(list_neighborhood)):
#         # print(sol[0])
#         # print(k)
#                 drone_neighborhood = list_neighborhood[k](sol[0])
#                 min_in_loop = 1000000
#                 next_index = 0
#                 if len(drone_neighborhood) == 0:
#                         continue
#                 for l in range(len(drone_neighborhood)):
#                         cfnode = drone_neighborhood[l][1][0]
#                         if cfnode - min_to_improve < epsilon:
#                                 aa = drone_neighborhood[l]
#                                 next_index = l
#                                 min_in_loop = cfnode
#                                 min_to_improve = cfnode
#                                 j = 0
#                         elif cfnode - min_in_loop < epsilon:
#                                 next_index = l
#                                 min_in_loop = cfnode
#                 sol = drone_neighborhood[next_index]
#         print("======")
#         print(sol[0][0])
#         print(sol[0][1])
# print("======")              
# print(sol[0])

# New_solution1 = [[[[0, [0, 0, 1]], [1, []], [5, [5, 13, 11]], [13, []], [14, [14]], [9, [9, 12, 15, 10]], [11, []], [15, []], [12, []], [10, []], [0, [2, 8]], [6, [6, 7, 3, 4]], [7, []], [8, []], [4, []], [3, []], [2, []]]], 
#                  [[[5, [5, 13, 11]]], [[14, [14]]], [[9, [9, 12]]], [[6, [6, 7, 3, 4]]]]]
# ChangePackages = [15, 10]
# ChangeInTruck = 0
# l = 5

# New_solution1, index_drone_trip, index_in_trip, if_group = Neighborhood.groupTripInDroneRoute(New_solution1, ChangePackages, ChangeInTruck, l)

# solution = [[[[0, [0, 0, 1]], [1, []], [5, [5, 13, 11]], [13, []], [14, [14]], [9, [9, 12, 15, 10]], [11, []], [15, []], [12, []], [10, []], [0, [2, 8]], [6, [6, 7, 3, 4]], [7, []], [8, []], [4, []], [3, []], [2, []]]], 
#             [[[5, [5, 13, 11]]], [[14, [14]]], [[9, [9, 12, 15, 10]]], [[6, [6, 7, 3, 4]]]]]
# i = 2
# solution, index = Neighborhood.updateDroneQueueReturnNewIndex(solution=solution, index_trip=i)
# print(solution)

# Nei =Neighborhood_drone.Neighborghood_change_drone_route_max_pro_plus(new_)
# Nei, solution_pack = Neighborhood.Neighborhood_combine_truck_and_drone_neighborhood_with_package(name_of_truck_neiborhood=Neighborhood10.Neighborhood_one_opt_standard, solution=solution, number_of_potiential_solution=1, number_of_loop_drone=2, whether_use_truck_time=False, solution_pack=[], solution_pack_len=5, use_solution_pack=True, index_consider_elite_set=0)
Nei = Neighborhood.swap_two_array(new_)
# print(Nei[0][0])
for i in range(len(Nei)):
        if i == 72:
                print("-----------------------", i)
                print(Nei[i][0][0])
                print(Nei[i][0][1])
# solution_wr = [[[[0, [1]], [11, [11, 7, 4, 6, 8, 2, 14, 12, 9, 5, 10, 3]], [7, [13]], [8, []], [4, []], [5, []], [10, []], [15, []], [1, []], [2, []], [6, []], [14, []], [12, []], [9, []], [13, []], [3, []], [0, []]]],
#         [[[7, [13]]], [[11, [4, 10, 3]]], [[11, [7, 14, 5]]], [[11, [6, 8, 12, 9]]], [[11, [11, 2]]]]]

# solution_ww = [[[[0, [1]], [11, [11, 7, 4, 6, 8, 2, 14, 12, 9, 5, 10, 3]], [7, [13]], [8, []], [4, []], [5, []], [10, []], [15, [15]], [1, []], [2, []], [6, []], [14, []], [12, []], [9, []], [13, []], [3, []], [0, []]]], [[[7, [13]]], [[11, [4, 10, 3]]], [[11, [7, 14, 5]]], [[11, [6, 8, 12, 9]]], [[11, [11, 2]]]]]

# new_hehe = Neighborhood.findLocationForDropPackage(solution_wr,0, 15)
# new_solution, number_in_the_drone_queue_of_drop_package, index_in_trip = Neighborhood.addNewTripInDroneRoute(solution_ww, [15], 0, 7)

# print(new_solution)
# print(Function.fitness(solution))