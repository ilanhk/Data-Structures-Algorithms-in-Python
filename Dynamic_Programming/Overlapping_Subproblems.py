# Two things that are required for dynamic programing:
#  - Overlapping Subproblems 
#  - Optimized Structure


# Overlapping Subproblems (OS):
# its similar to breaking a problem in mutiple pieces solve each small piece and bring them all back together to solve the problem
# with OS when you break the problem to little subproblems. Some of the subproblems maybe the same problem to solve.
# When we say OS it means repeating subproblems.

# lets say a subproblem that repeats has a trilion operations to solve the problem, when its done running it returns 10.
# then we go to the next identical subproblem we already know it will return 10 and it will be very ineffiecient to do those trilion operations again.

# one of the things we can do is take 10 and store it in a list. Lets say its subproblem 1 so we put 10 in the index of 1.
# so when we move to the next identical subproblem we can see if we have a value at the index of 1 instead of running a trilion operations.
# This makes it o(1)
# then if we find a next non identical subproblem and it returns 20 we would put 20 at index 2 ...etc 
# this method is called Memoization not "memerizatrion"

# Merge sort has subproblems but not Overlapping Subproblems. BC:
# - subproblems are not identical/repeating they are unique they dont "Overlap"



