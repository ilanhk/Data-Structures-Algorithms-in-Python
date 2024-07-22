# if you have 2 sorted lists its very easy to combine them to a new sorted list
# if we have an unsorted list of 8 items what merge sort would do its break it in half, break it in half again and again until we have lists that have only 1 item in them.
# there will be 8 seperate lists with one item in each. 
# A list with 1 item in it by definition its sorted.
# then we merge the lists to have two sorted items in each list then merge to 4 items in each list then finally merge to one sorted list with 8 items

# Merge is a helper function doesnt do the whole merge sort it does a portion of it

def merge(list1, list2):
  combined = []
  
  i = 0
  j = 0 
  
  while i < len(list1) and j < len(list2): #if any of the lists becomes empty the while loop would break
    if list1[i] < list2[j]:
      combined.append(list1[i])
      i += 1
    else:
      combined.append(list2[j])
      j += 1
  
  while i < len(list1):
    combined.append(list1[i])
    i += 1
    
  while j < len(list2):
    combined.append(list2[j])
    j += 1
    
  return combined
  # cant use for loops when combinding list1 and list2 bc we dont know how many of each to take from each list better to use while loops
  
# print(merge([1,2,7,8], [3,4,5,6]))


# after the list is broken down to lists with 1 item in each we will use the merge function to put it back together
# recursion will be used to break the list smaller and smaller

def merge_sort(my_list):
  if len(my_list) == 1:
    return my_list
  mid_index = int(len(my_list)/2) # if the list is an odd number it will give us an int ex int(3/2) = 1 not 1.5 bc decimal will be droped
  left = merge_sort(my_list[:mid_index]) #from 0 to mid_index anything left of ":" is the max range
  right = merge_sort(my_list[mid_index:]) # the opposite mid_index is the staring point it will go to the end of the list
  
  return merge(left, right)

original_list = [3,1,4,2]
sorted_list = merge_sort(original_list)

print('Original', original_list)
print('Sorted', sorted_list)

# Merge Sort Big O:
# space complexity - start with one list until each list has one of its item so list stored in memory has doubled which is o(n)
#  time complexity - when we break in half each time it adds a step which is o(log n) but when we start puting the halves back together with while loops its o(n)
# so together in time complexity - its o(n log n) - its less efficent than o(n) but more efficient than o(n^2)