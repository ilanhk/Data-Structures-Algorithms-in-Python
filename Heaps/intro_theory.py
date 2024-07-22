# Heaps are very similar to a binary search tree but the numbers are not distributed in the same order

# A heap is a complete tree

# The highest value will always be at the top lowest at the bottom this is called a "Max Heap"
# each node value will be greater or equal than the value of its decendences (duplicates are allowed)
# the opposite is called a "Min Heap"
# for Max or Min Heap no specific order on how decendence are organised left or right. if its max the top is at the top bottom at the bottom etc..
# bc of that Heaps are not good for searching. Only use a Heap to keep the largest item at the top to qucikly remove it.

# another difference between a heap and binary search trees are that heaps are stored in a list instead of a class
# list will only store integers. 
# Value of the root is either stored at index 0 or 1.

# to store root at index 1 we can do this math:

# to find a left child = 2 * parent_index
# to find the right child = (2 * parent_index) + 1

# to find a parent of 2 nodes its child_node/2 if its 3.5 we will consider it 3


# Priority Queues & Big O:
# Priority Queues - if you say that the highest value is the highest priority and you always want to remove the highest value of a queue than a heap is a very great way in doing this
# heap is more efficient to do this over a linked list because better Big O
# a dictionary o(1) would be more efficient than a Heap if you know the specific value you are looking for
# binary search tree o(log(n)) would be more efficient than Heap only if the BST is balance
# For a Heap insert or remove will always be o(log(n)) which is incredibly efficient

