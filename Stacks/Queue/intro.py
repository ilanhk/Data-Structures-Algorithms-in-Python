# queues is like a regular queue if you are the first person you will be the first person to get out of the line
# FIFO (first in first out)
# when you add people to the queue its called "Enqueue"
# when you remove people from the queue its called "Dequeue"
# you can use a linked list for a queue but instead of head and tail we will use first and last

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    
class Queue:
  def __init__(self, value):
    new_node = Node(value)
    self.first = new_node
    self.last = new_node
    self.length = 1
    
  def print_queue(self):
    temp = self.first
    while temp is not None:
      print(temp.value)
      temp = temp.next
  
  # this is an o(1) from the last
  def enqueue(self, value):
    new_node = Node(value)
    if self.first is None: 
      self.first = new_node
      self.last = new_node
    else:
      self.last.next = new_node
      self.last = new_node
    self.length += 1
    
  # this is an o(1) from the first
  def dequeue(self):
    if self.length == 0:
      return None
    temp = self.first
    if self.length == 1:
      self.first = None
      self.last = None
    else:
      self.first = self.first.next
      temp.next = None
    self.length -= 1
    return temp
    

my_queue = Queue(4)
# my_queue.enqueue(5)
# my_queue.enqueue(6)
my_queue.dequeue()
my_queue.print_queue()