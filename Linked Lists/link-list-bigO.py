# to add/append something to a linked list its o(1) - if you added to the front or end of the list
# to remove/pop from the end of the list its o(n) bc once you pop a node the tail needs to find a new node to point to
# to remove from the front of the list it will be o(1) - to do this need to have head point at the next node
# adding item in middle of the list its o(n)- 1st you need to find the head and iterate through the list until we get to that specific node, then set the pointer of the new node to after the specific node and the specific node point to the new node to add it in.
# removing a node in the middle of the list its o(n) - need to interate from the head find the node to remove the node before make it point to the node after the node for removal then you can remove the node
# look up with a link list either by value or index its o(n) - need to iterate from the head till you find the node