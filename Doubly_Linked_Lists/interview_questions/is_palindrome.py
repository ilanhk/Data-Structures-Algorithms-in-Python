# DLL: Palindrome Checker ( ** Interview Question)
# Write a method to determine whether a given doubly linked list reads the same forwards and backwards.

# For example, if the list contains the values [1, 2, 3, 2, 1], then the method should return True, since the list is a palindrome.

# If the list contains the values [1, 2, 3, 4, 5], then the method should return False, since the list is not a palindrome.

# Method name:
# is_palindrome

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
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
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    # WRITE IS_PALINDROME METHOD HERE #
    
    def is_palindrome(self):
        if self.length <= 1:
            return True
        forward_node = self.head
        backward_node = self.tail
        for _ in range(self.length // 2): # The // operator is the floor division operator, which divides self.length by 2 and rounds down to the nearest integer.
            if forward_node.value != backward_node.value:
                return False
            forward_node = forward_node.next
            backward_node = backward_node.prev
        return True
    ###################################