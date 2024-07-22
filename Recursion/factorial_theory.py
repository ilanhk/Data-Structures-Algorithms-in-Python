# Factorials are a good way to teach Recursion
# a factorial for ex: 
# 4! = 4 * 3 * 2 * 1
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1 - this is the "Base Case"
# factorials are recursive because the process is the same until 1. 
# Also the problem gets smaller until you reach the "Base Case"

# This is the Recursive function for Factorial:
def factorial(n):
  if n == 1:
    return 1
  return n * factorial(n-1)

print(factorial(4))
# in this case the call stack 1! is called first than 2! than 3! and 4! is at the botom of the call stack
