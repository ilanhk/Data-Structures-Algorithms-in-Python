# o(n^2) or o(n*n)  is a lot less efficient of a time complexity stand point compared to o(n)
#example of o(n^2):


# def print_items(n):
#     for i in range(n):
#        for j in range(n):
#         print(i,j)
    
      

# Drop non Dominance: 
# In this function there is an extra 0(n) operation. Technically this would be o(n^2 + n)
# but because n^2 is more significant(dominant) and the +n would be non dominate it would still be o(n^2):

def print_items(n):
    for i in range(n):
       for j in range(n):
        print(i,j)
    for k in range(n):
        print(k)
        


print_items(10) 