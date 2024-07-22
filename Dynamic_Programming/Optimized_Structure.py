# Optimized Structure is the 2nd requirement for dynamic programing
# Optimized Structure - means Optimal solution

# if you continue the subproblems if you have an optimal solution of solving subproblem 1 , 2 and 3 etc 
# that would give us the optimal solution to the overall problem when combining all subproblems

# another good representation of Optimized Structure is weighted graph
# A -> B 10,  B -> D 15,  C -> D 20,  A -> C 30
# - Lets say we want to go to  to A to D with the lowest cost path.
# A -> B 10,  B -> D 15 = 25 both weights are cost less so optimal. 
# If you have an optimal way of going A -> B and B -> D it give us the optimal way of going to A to D

# What does not have an optimal substructure:
# A to D the highest cost path - A -> C 30 and C -> D 20 - there is no overlapp and no retracing
# Higest cost path to A -> C is not going direct but A -> B 10,  B -> D 15,  D -> C 20 - cant take the optimial solution to each subproblem