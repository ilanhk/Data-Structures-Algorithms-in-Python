# Hash Tables Linked Lists Big O

# Big O of the hash method itself - o(1) becuase same operation for any key you put in it

# appending to a link list in a hash table is also o(1)

# get_item(key) would be o(1) if there is only 1 node in the address if multiple nodes it will be o(n). 
# But because collisions would be very rare bc there would usually be a lot more address spaces
# we will assume its 0(1) when using get_item(key)

# In general we treat Hash Tables as o(1) because everything you do with hash tables is o(1)