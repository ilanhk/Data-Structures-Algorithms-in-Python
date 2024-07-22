# there are 2 approaches 

# nested for loop - o(n^2) - The Naive way
# def item_in_common(list1, list2):
#   for i in list1:
#     for j in list2:
#       if i == j:
#         return True
#   return False


# using dictionaries - o(n) - The most efficent way for this problem
def item_in_common(list1, list2):
  my_dict = {}
  
  for i in list1:
    my_dict[i] = True
    
  for j in list2:
    if j in my_dict:
      return True
    
  return False




list1 = [1,3,5]
list2 =[2,4,5]

print(item_in_common(list1, list2))

