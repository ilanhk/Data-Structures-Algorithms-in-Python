# In dynamic programing there are 2 different ways of solving problems:
#  - Top Down
#  - Bottom Up

# when we did Fibonacci Sequence(FS) recursively it was "Top Down" 
# the first thing we tried to solve is the highest number ex fib(7) then we would go all the way down to fib(0) on the call stack

counter = 0 

# This code is Fibonacci Sequence(FS) but bottom up:
def fib_bottom_up(n):
  global counter 
  fib_list = [0,1]
  
  for index in range(2, n+1): # range(2, n+1) -starting with 2 because we need to calculate from index 2
    counter += 1
    next_fib = fib_list[index - 1] + fib_list[index - 2]
    fib_list.append(next_fib)
  
  return fib_list[n]

# this is o(n-1) which is o(n)
# if fib_list = [0,1] was stored outside the func we can do memoization and make it o(1)
# The pronlem of Memoization is that you would have to store the list permanently outside in memory. Can be useful or not depending on the situation


z = 35

print('Fib of', z, '=', fib_bottom_up(z))
print('number of func calls: ', counter)

    
