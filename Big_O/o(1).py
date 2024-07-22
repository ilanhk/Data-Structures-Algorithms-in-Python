# o(1) means 1 operation or contanst time - its the most efficient big o
# example:

# def add_items(n): 
#     return n+n 
# this function is o(1) because its just one operation 

def add_items(n): 
    return n+n+n
# even if you add an extra +n it will still be o(1) which is why its constant 