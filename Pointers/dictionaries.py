dict1 = {
  'value': 11
}

dict3 = {
  'value': 44
}

dict2 = dict1 #it eill still point to the same dict1 in memory

print('B4 the update')
print('dict1: ', dict1)
print('dict2: ', dict2)


print('dict1 points to: ', id(dict1) , 'the address where its stored in memory')
print('dict2 points to: ', id(dict2) , 'the address where its stored in memory')

dict2['value'] = 22 #this will update dict1 also because it will change the same obj in memory instead of making a new obj

print('After the update')
print('dict1: ', dict1)
print('dict2: ', dict2)

print('dict1 points to: ', id(dict1) , 'the address where its stored in memory')
print('dict2 points to: ', id(dict2) , 'the address where its stored in memory')


dict2 = dict3
dict1 = dict2
# after this change we wont have access to {'value': 11} in memory bc no variable is pointing to it
# python will remove {'value': 11} through a process called 'Garbage Collection'


print('After the update including dict3')
print('dict1: ', dict1)
print('dict2: ', dict2)
print('dict3: ', dict3)

print('dict1 points to: ', id(dict1) , 'the address where its stored in memory')
print('dict2 points to: ', id(dict2) , 'the address where its stored in memory')
print('dict3 points to: ', id(dict3) , 'the address where its stored in memory')
