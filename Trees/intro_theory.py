# its a linked list that forks
# binary tree will have nodes that have left and right, they can only point to 2 nodes
# trees dont have to be binary, a node could point to 3 nodes instead of 2 etc
# In a "Full" tree every node points to no nodes or all nodes (binary only 2 nodes) If not all nodes point to other nodes the tree is not full
# for binary if not all nodes points to 2 nodes the tree is not full
#  a "Perfect" tree is where all nodes are full and symetrical the tree becomes "Complete"
# "Complete" tree you are filling a tree from left to right with no gaps
# Top node is called a parent the nodes under are children and siblings. 
# There is only one parent node at the top in a Tree. Or else its not a tree.
# a child node can become a parent node if it has children
# Nodes with no children are called leafs

# Binary Search Trees(BST) are different to Binary trees bc for BST if the node is greater than the top node it will be a child on the right side. If its less than it will be on the left.
# for BST it will always check the node from the top if the node to add is greater but their is a node filled up on the right it will check if its greater or less than the node already added and becomes its child accordingly
# after filling up a BST all nodes from the right will be greater than the parent at the top. All nodes on the left of it is least than.

# BST Big O
# the top is 2^1 -1, second layer is 2^2 -1. the 3rd layer is 2^3 -1 ...etc
# Cant have duplicate nodes in a BST
# we will remove -1 bc of the big O rules so 2^1 (1 step) , 2^2 (2 steps), ...etc
# if we are in the 4th layer 2^4 it would take 4 steps to remove or add a node.
# so BST is O(log n) which is very efficient (Divide and Conqueor)
# if a tree is just a line of greater than its a linked list so O(n) its the worst possible scenario
# in a BST for insert(), remove() and lookup() we treat it as  O(log n)
# insert is faster in a linked list than BST because its o(1) but lookup() and remove() is better in a BST than a LL bc its O(log n) instead of o(n)


 