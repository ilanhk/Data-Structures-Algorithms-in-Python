# o(n) means the number of operations is proportionate to n. 
#example

# def print_items(n):
#     for i in range(n):
#         print(i)
         


# Drop constants - In the code bellow its the same operation twice in one function its still o(n) instead of 0(2n)
#example

def print_items(n):
    for i in range(n):  # o(n)
        print(i)
    for j in range(n):  # o(n)
        print(j)
        
# this would be o(n+n) = o(2n) but we would drop the 2 constant = o(n)


print_items(10) 

# Different terms for  inputs
# However if we have different terms for inputs example: 

def print_items(a,b):
    for i in range(a):  # its not o(n) its o(a)
        print(i)
    for j in range(b):  # its not o(n) its o(b)
        print(j)
        
# so it will be o(a+b)

# if its nested like this
def print_items(a,b):
    for i in range(a):
       for j in range(b):
        print(i,j)
        
# This would be o(a*b)
