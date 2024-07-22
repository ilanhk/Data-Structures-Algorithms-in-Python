# same as the stack section image a tennis ball box - only the top gets removed first
# ex:

def funcThree():
  print('Three')

def funcTwo():
  funcThree()
  print('Two')

def funcOne():
  funcTwo()
  print('One')
  
  

  
funcOne()
  
# funcOne() is at the bottom of the stack then its funcTwo() in the middle and funcThree() at the top.
# bc 'Three' will be printed first, funcThree() is done running so we can pop it out from the call stack than 'Two' than finally 'One'