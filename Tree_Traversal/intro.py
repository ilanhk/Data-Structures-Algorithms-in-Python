
# All are methods in a Binary Search Tree class

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
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
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
      
    # Breath First Search (BFS)
    def BFS(self):
      current_node = self.root
      queue = []
      results = []
      queue.append(current_node) #need to put current node in the queue b4 start while loop
      while len(queue) > 0:
        current_node = queue.pop(0) #first item in the queue (its also includes the values of left and right)
        results.append(current_node.value)
        if current_node.left is not None:
          queue.append(current_node.left)
        if current_node.right is not None:
          queue.append(current_node.right)
      return results
  
  
    # Depth First Search - Pre Order
    # bc there is recursion it will use a call stack
    def dfs_pre_order(self):
        results = []
        
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root)
        return results
    
    
    # Depth First Search - Post Order
    # it will go left all the way to the bottom take the farthest left then it will go up one an go right if there is an find the farthest left or right
    # then it goes up its gone left and right already so it will add that to the list and go up then it will go right and repeat the process again
    # the root will be added last to the list
    # bc there is recursion it will use a call stack
    def dfs_post_order(self):
        results = []
        
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
            # same code just in a different order append to results at the end of all if statments
            
        traverse(self.root)
        return results
    
    
    # Depth First Search - In Order
    # first go all the way to the farthest left take that then go up take that then go right take the right if nothing else
    # then take the top and go right and repeat process
    # the list will look like from lowest value to highest (numerical order)
    def dfs_in_order(self):
        results = []
    
        def traverse(current_node):
            
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value) 
            if current_node.right is not None:
                traverse(current_node.right)
            # again same code just in a different order append to results at the end of all if statments
        
        traverse(self.root)
        return results
    

    
          
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
        
print(my_tree.BFS())
print(my_tree.dfs_pre_order())
print(my_tree.dfs_post_order())
print(my_tree.dfs_in_order())