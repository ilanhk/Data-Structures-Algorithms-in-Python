# Recursion is a function that calls itself ... until it doesnt
# ex if you have a gift box and you have open_giftbox() it will either give you a ball or another but smaller giftbox
# to open the returned giftbox you will need to use the same open_giftbox() and again it will either return a ball or another smaller giftbox
# then you run open_giftbox() agan then you are left with a ball

# this ex code will give us an idea but its Psuedo code (its not ment to work just give an idea):
def open_giftbox():
  if ball:
    return ball 
  open_giftbox()
  
# when opening each new box using the same function.
# The idea is the process of whatever we are doing with recursion needs to be the same.
# each time we open a box we make the problem smaller
# if we open a box and it becomes a ball its called the "Base Case" (function will stop calling itself) -the if statement is the base case
# if the function needs to call itself again its "Recursive Case"
# If we dont have a base case in a recursive function (no if ball statement) it will become a "Stack Overflow"
# the if statement must be true at some point. If not its a Stack Overflow
# Also must have a return statement in the if statment. Or else it wont stop the code and cause a Stack Overflow

  