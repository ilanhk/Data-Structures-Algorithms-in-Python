#  Stacks are like adding tennis balls in its tube. You can only add and remove balls from the top
# if you have 3 balls in a stack to get to the first one you droped in you need to start from the last ball on the top then the second
# You can use a linked list to implement a stack where you can only add and remove from the head end bc removing and adding from the head is 0(1)
# with a stack only removing from the top so no self.tail / self.bottom variable

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    
class Stack:
  def __init__(self, value):
    new_node = Node(value)
    self.top = new_node
    # self.bottom = new_node # we dont need this because only adding and removing from the top
    self.height = 1
    
  def print_stack(self):
    temp = self.top
    while temp is not None:
      print(temp.value)
      temp = temp.next
      
  # This is an o(1)
  def push(self, value):
    new_node = Node(value)
    if self.height == 0:
      self.top = new_node
    else:
      new_node.next = self.top
      self.top = new_node
    self.height += 1
    
  # this is an o(1)
  def pop(self):
    if self.height == 0:
      return None
    temp = self.top
    self.top = self.top.next
    temp.next = None
    self.height -= 1
    return temp


my_stack = Stack(4)
# my_stack.push(5)
# my_stack.push(6)
my_stack.pop()
my_stack.print_stack()
    
