# we start with a pivot point which is the first item in a list then we go to all items in the list and compare 
# the bigger item will be marked then we move to the next item if its smaller than the bigger item it will swap positions
# eventually all items smaller than the first item are together and all items greater than the first item are together
# then we will swap the first item with the last less than item.
# the first item x is sorted. Everything left of x is left and right of x is right.
# than the left first item will be the pivot and move swap with the lesser item to be sorted. Same thing with the right.
# eventually the whole list will be sorted in order

# Pivot function will be a helper func for quick sort
# Pivot will always be the first item in the array y. Then it will sort all items less than y on the left and greater than y on the right.
# the pivot will be put between the left and the right then return the index of y. 
 
def swap(my_list, index1, index2):
  temp = my_list[index1]
  my_list[index1] = my_list[index2]
  my_list[index2] = temp
  
def pivot(my_list, pivot_index, end_index):
  swap_index = pivot_index
  
  for i in range(pivot_index+1, end_index+1):
    if my_list[i] < my_list[pivot_index]:
      swap_index += 1
      swap(my_list, swap_index, i)
  swap(my_list, swap_index, pivot_index)
  return swap_index

mlist = [4,6,1,7,3,2,5]

# print(pivot(mlist, 0, 6))
# print(mlist)


def quick_sort_helper(my_list, left, right): #left is the most left index the lowest, right is the most right index the highest
  if left < right:
    pivot_index = pivot(my_list, left, right)
    quick_sort_helper(my_list, left, pivot_index-1)
    quick_sort_helper(my_list, pivot_index+1, right)
  return my_list

def quick_sort(my_list): #made this function so we dont need to add the beginning and end index when we run it
    return quick_sort_helper(my_list, 0, len(my_list)-1)

print(quick_sort(mlist))


# Big O Quick Sort:
# pivot func has a for loop going through all the list looking at each item - so its o(n)
# the recursive part o(log n)
# so quick sort is o(n log n
# however the worst case is if we already have a sorted list bc we would run pivot func on every single item which would be o(n^2)
# if we have sorted data better to use insertion sort its more efficient
  
  
  

