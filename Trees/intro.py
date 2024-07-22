class Node:
  def __init__(self, value):
    self.value = value
    self.left = None 
    self.right = None

class BinarySearchTree:
  
  # Create a tree with a starting node
  # def __init__(self, value):
  #   new_node = Node(value)
  #   self.root = new_node # root is the node at the top
    
  # Or you can create a tree without a starting node
  def __init__(self):
    self.root = None
    
    
  def insert(self, value):
    new_node = Node(value)
    if self.root is None:
      self.root = new_node
      return True #so code will end here
    temp = self.root
    while (True): # this loop wont stop until you add a return statement
      if new_node.value == temp.value:
        return False
      if new_node.value < temp.value:
        if temp.left is None:
          temp.left = new_node
          return True
        temp = temp.left
      else:
        if temp.right is None:
          temp.right = new_node
          return True
        temp = temp.right
        
    
  def contains(self, value):
    # if self.root is None: # you dont need this if statement but its a good why to show the thought process
    #   return False
    temp = self.root
    while temp is not None: #bc if temp is None we reached the end of the tree
      if value < temp.value:
        temp = temp.left
      elif value > temp.value:
        temp = temp.right
      else:
        return True
    return False
  
        
        

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)



# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)
print(my_tree.contains(27))
print(my_tree.contains(77))

  
