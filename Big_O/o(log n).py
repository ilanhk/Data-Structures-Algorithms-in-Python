# Lets say we want to look for 1 in this array:
arr = [1,2,3,4,5,6,7,8]

# The most efficient way to get it is to cut the array in half each time to find it example:
arr = [1,2,3,4,5,6,7,8]

arrA = [1,2,3,4]
arrB = [5,6,7,8] # 1 is not here

# from arrA = [1,2,3,4]

arrAB = [3,4] # 1 is not here

# from arrAA = [1,2]
arrAAA = [1] # 1 is here
arrAAB = [2] # 1 is not here

#for this case this took us 3 steps to find 1 from 8 items 
# also its so happens that 2^3=8 which is also log₂8 = 3 (this also means how many times you divide 8 by 2 to get to one item. its 3 times)
# but if you have billion items in an array how to find one item? log₂1,000,000,000 =31 steps. 
# Its more effiecient to have 31 steps that 1 billion steps hence o(log n)
# o(log n) is not as effiecient as o(1) but its more efficient than o(n)
# o(nlog n) is more efficient than o(n^2) but less effiecient of o(n) but its the most efficient for sorting algorithms





