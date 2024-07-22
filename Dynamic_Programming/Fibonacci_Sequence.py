# Fibonacci Sequence(FS)
# taking 2 previous numbers and adding it together
#  1+1 = 2, 2 is the next number in the sequence, then 1 + 2 and get 3, 2 + 3 is 5  ...etc
#  in math FS usually starts with 1 but in computer science it starts with zero

counter = 0

def fib(n):
  global counter # allows us to see the variable outide of the func.
  counter += 1
  if n == 0 or n ==1:
    return n
  return fib(n-1) + fib(n -2)


# print(fib(0))
# print(fib(1))
# print(fib(2))
# print(fib(3))
# print(fib(4))
# print(fib(5))


z = 7

print('Fib of', z, '=', fib(z))
print('number of func calls: ', counter)


# FS - has overlapping problems and optimize substructure
#  but FS in this way is o(2^n) which is less efficient than o(n^2) so very inefficient'

# Memoization will make FS more efficient especially with recursion 


memo = [None] * 100 # init 100 indexs of a list with None
counter_with_memo = 0

def fib_with_memo(n):
  global counter_with_memo 
  counter_with_memo += 1
  
  if memo[n] is not None:
    return memo[n]
  
  if n == 0 or n ==1:
    return n
  
  memo[n] = fib_with_memo(n-1) + fib_with_memo(n -2) 
  
  return memo[n]

# Big O of FS with Memoization is o(2n-1) which is o(n)
# if using recursion it will be very inefficient if you dont use some sort of memoization


print('Fib with Memo of', z, '=', fib_with_memo(z))
print('number of func calls with memo: ', counter_with_memo)

