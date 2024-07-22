# If we have a list if the first item is bigger than the second item thet will switch positions it will keep doing this until the biggest item has been sorted or "Bubbled Up". 
# It will continue this trend until the list is sorted from smallest to largest

def bubble_sort(list):
  for i in range(len(list) -1 , 0, -1):
    for j in range(i):
      if list[j] > list[j+1]:
        temp = list[j]
        list[j] = list[j+1]
        list[j+1] = temp
  return list
# range(len(list) -1 , 0, -1) means the range is the length of the list -1, we will start at zero and decrement each time by -1
    
print(bubble_sort([4,2,6,5,1,3]))