# Linked lists are lists with no indexes
normal_list = [1,2,3] # has indexes and each item is saved in memory in that order (contiguous) which is why there is an index
# with a linked list all of the items/nodes will be spread out in memory 
# link lists have a variable called 'head', it points to the first node 
# and another variable called 'tail' it points to the last node
#each node points to the next node in the link list the last node will point to none
# a node is value + pointer (its a dictionary)
node_ex = {
  "value": 4,
  "next": None
}

# link list is similar (nested dictionaries)
head = {
  "value": 11,
  "next": {
    "value": 3,
    "next": {
      "value": 23,
      "next": {
        "value": 7,
        "next": None
      }
    }
  }
}

# print(head['next']['next']['value'])

# this will only run in a linked list its a set of nested dictionaries
# print(my_linked_list.head.next.next.value)

# class LinkedList:
  # def __init__(self, value):
    # create a new node 
    # initialize a new linked list
    
  # def append(self, value):
    # create a new node
    # add it to the end
    
  # def prepend(self, value):
    # create a new node
    # add it to the begining 
  
  # def insert(self, index, value):
    # create a node 
    # insert node in an index or where you want  
   
#problem is all these methods would create a new node better to call on the Node class to create it

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
# this class will only contain a contructor to make a new node

class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1
    
  def print_list(self):
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next
      
  def append(self, value):
    new_node = Node(value)
    
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1
    return True # not necessary but nessary for another upcoming function
    
  def pop(self):
    if self.length == 0:
      return None
    temp = self.head
    pre = self.head
    
    while (temp.next):
      pre = temp
      temp = temp.next
    self.tail = pre
    self.tail.next = None 
    self.length -=1
    
    if self.length == 0:
      self.head = None
      self.tail = None
    
    return temp

  def prepend(self, value):
    new_node = Node(value)
    
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    self.length +=1
    return True # not necessary but nessary for another upcoming function
  
  def pop_first(self):
    if self.length == 0:
      return None
    else:
      temp = self.head
      self.head = self.head.next
      temp.next = None
      self.length -= 1
      if self.length == 0:
        self.tail = None
      return temp 
  
  def get(self, index):
    if index < 0 or index > self.length:
      return None
    temp = self.head
    for _ in range(index): #usually we put a variable i in the forloop but because we are not using the variable, we replace the variable with: _
      temp = temp.next
    return temp
  
  def set_value(self, index, value):
    temp = self.get(index)
    if temp:
      temp.value = value
      return True
    return False
  
  def insert(self, index, value):
    if index < 0 or index > self.length:
      return False
    if index == 0:
      return self.prepend(value)
    if index == self.length:
      return self.append(value)
    new_node = Node(value)
    temp = self.get(index - 1)
    new_node.next = temp.next
    temp.next = new_node
    self.length += 1
    return True
  
  def remove(self, index):
    if index < 0 or index >= self.length:
      return None
    if index == 0:
      return self.pop_first()
    if index == self.length:
      return self.pop()
    prev = self.get(index - 1)
    temp = prev.next
    prev.next = temp.next
    temp.next = None
    self.length -=1
    return temp
  
  #common interview question
  def reverse(self):
    temp = self.head
    self.head = self.tail
    self.tail = temp
    after = temp.next
    before = None 
    for _ in range(self.length):
      after = temp.next
      temp.next = before
      before = temp
      temp = after
    
    
      
  
    
  
  
         
    
my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(75)
my_linked_list.prepend(5)
my_linked_list.insert(2, 100)
# my_linked_list.pop()

my_linked_list.set_value(1, 85)

my_linked_list.remove(2)

my_linked_list.print_list()
# my_linked_list.pop_first()
# my_linked_list.print_list()
# print(my_linked_list.get(0))

my_linked_list.reverse()

my_linked_list.print_list()

