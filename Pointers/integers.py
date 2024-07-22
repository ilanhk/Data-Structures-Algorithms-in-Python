num1 = 11 

num2 = num1

print('B4 num2 value is updated:')
print('num1: ', num1)
print('num2: ', num2)

print('num1 points to: ', id(num1) , 'the address where its stored in memory')
print('num2 points to: ', id(num2) , 'the address where its stored in memory')


num2 = 22

print('After num2 value is updated:')
print('num1: ', num1)
print('num2: ', num2)

print('num1 points to: ', id(num1) , 'the address where its stored in memory')
print('num2 points to: ', id(num2) , 'the address where its stored in memory')




