# classes are like cookie cutters 

class Cookie: 
  def __init__(self, color): # this is a constuctor every time we make a new instance of a class this will be called
    self.color = color
  
  def get_color(self):
    return self.color
  
  def set_color(self, color):
    self.color = color
    
    
cookie_1 = Cookie('blue')
cookie_2 = Cookie('red')

print('cookie 1:', cookie_1.get_color())
print('cookie 2:', cookie_2.get_color())

cookie_1.set_color('green')

print('cookie 1 is now', cookie_1.get_color())