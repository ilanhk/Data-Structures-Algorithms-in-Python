# If we have a list:
my_list = [11,3,23,7]
#        0,1, 2,3

# if you look for a value in this list like 7
# if you loop until reach 7 its o(n)
# but if you want to find 7 by index and you want the value that its at the index 3 that is o(1)

my_list.append(17) #adds to the end of the list
# Or
my_list.pop() #removes the added 17 from the end of the list

# you are not changing the list just adding 1 or removing the one added its o(1).



# but if you pop the 1st index 11 is 3 not index 1 anymore it will change to index 0, so on with the other numbers
my_list.pop(11)
# same is true if we bring 11 back to index 0, you will need to change the index of 3 to index 1 ans so on
my_list.append(0,11)

# both these senarios are o(n) n would be the # of items in the list


# but if you insert something in the middle of the list example:
my_list.append(1,'Hi')
# index of 11 is not changed but the index of 3 and the rest of the list is changed
# even though this would be o(1/2n) its still o(n) bc droping constants
# same is true if we remove 'Hi'

