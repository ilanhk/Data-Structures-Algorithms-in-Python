# The difference between bubble sort and selection sort is you will need indexes for selection sort
# first we check the first item and find the min_index (its the index where the minimum value is)
# we will go through the whole list and find the min_index if a value is smaller we will say its index is minimum
# then after going through the whole list we switch the values of the first index and the minimum and repeat the process

def selection_sort(my_list):
  for i in range(len(my_list)-1):
    min_index = i
    for j in range(i+1, len(my_list)):
      if my_list[j] < my_list[min_index]:
        min_index = j
    if i != min_index:
      temp = my_list[i]
      my_list[i] = my_list[min_index]
      my_list[min_index] = temp
  return my_list
  # range(i+1, len(my_list)) means - i+1 is our start value and len(my_list) is the our end value in the for loop
      
print(selection_sort([4,2,6,5,1,3]))