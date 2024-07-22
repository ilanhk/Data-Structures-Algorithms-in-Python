# Always start with the second item in the list then compare it with the item b4 it. If its less than the item before we switch
# then we move to the next item and continue the process until you reach a special case that will go all the way to the begining

def insertion_sort(my_list):
  for i in range(1, len(my_list)):
    temp = my_list[i]
    j = i-1
    
    while temp < my_list[j] and j > -1: #index cannot be -1
      my_list[j+1] = my_list[j]
      my_list[j] = temp
      j -= 1
    
  return my_list

print(insertion_sort([4,2,6,5,1,3]))

# Big O of Insertion Sort:
# worst case its o(n^2)
# best case its o(n) - bc if you have a sorted or almost sorted list the time is minimum to complete the task