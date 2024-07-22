# root will be in index of zero instead of one the math will adjust to that
class MaxHeap:
  def __init__(self):
    self.heap = []
    
  def _left_child(self, index):
    return 2 * index + 1
  
  def _right_child(self, index):
    return 2 * index + 2
  
  def _parent(self, index):
    return (index -1) // 2 # // will divide and only give an integer no decimals
  
  def _swap(self, index1, index2):
    self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
  # for this method to be for a Minheap swap ">" to "<" 
  def _sink_down(self, index):
    max_index = index
    while True:
      left_index = self._left_child(index)
      right_index = self._right_child(index)
      
      if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
        max_index = left_index
      
      if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
        max_index = right_index
      
      if max_index != index:
        self._swap(index, max_index)
        index = max_index
      else:
        return #to break us out of the while loop
      
    
  
  def insert(self, value):
    self.heap.append(value)
    current = len(self.heap) -1 # to get the last index added
    
    while current > 0 and self.heap[current] > self.heap[self._parent(current)]: 
      self._swap(current, self._parent(current))
      current = self._parent(current)
    # if its a MinHeap just change self.heap[current] > self.heap[self._parent(current)] to self.heap[current] < self.heap[self._parent(current)]
      
      
  # When removing a item of a Heap always remove at the top. But once top is removed need to rearrange the heap to make the tree complete
  # this method would be exactly the same in a MinHeap
  def remove(self):
    if len(self.heap) == 0:
      return None
    
    if len(self.heap) == 1:
      return self.heap.pop()
    
    max_value = self.heap[0]
    self.heap[0] = self.heap.pop()
    self._sink_down(0)
    
    return max_value
    
    
    
  
      
      
my_heap = MaxHeap()

# my_heap.insert(99)
# my_heap.insert(72)
# my_heap.insert(61)
# my_heap.insert(58)

# print(my_heap.heap)

# my_heap.insert(100)

# print(my_heap.heap)

# my_heap.insert(75)

#my_heap.insert(99)

my_heap.insert(95)
my_heap.insert(75)
my_heap.insert(80)
my_heap.insert(55)
my_heap.insert(60)
my_heap.insert(50)
my_heap.insert(65)

print(my_heap.heap)

my_heap.remove()

print(my_heap.heap)

my_heap.remove()

print(my_heap.heap)










    