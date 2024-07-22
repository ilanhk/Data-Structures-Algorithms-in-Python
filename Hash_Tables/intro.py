# better to have a prime number of addresses

class HashTable:
  def __init__(self, size =7):
    self.data_map = [None] * size #create a list with 7 items in it and all of them will contain None
    
  def __hash(self, key):
    my_hash = 0
    for letter in key: 
      my_hash = (my_hash + ord(letter) * 23) % len(self.data_map) 
      #ord(letter) - returns the Unicode code(integer) point for a given character
      # 23 bc its a prime number
      # % - gives you the remander when you devide
    return my_hash
  
  def print_table(self):
    for i, val in enumerate(self.data_map):
      print(i, ": ", val)
  
  def set_item(self, key, value):
    index = self.__hash(key)
    if self.data_map[index] == None:
      self.data_map[index] = [] # this should happen only if the empty list hasnt been created
    self.data_map[index].append([key, value])
    
  def get_item(self, key):
    index = self.__hash(key)
    if self.data_map[index] is not None:
      for i in range(len(self.data_map[index])):
        if self.data_map[index][i][0] == key:
          return self.data_map[index][i][1] #return the value
    return None # if key not in the hash table
  
  def keys(self):
    all_keys = []
    for i in range(len(self.data_map)):
      if self.data_map[i] is not None:
        for j in range(len(self.data_map[i])):
          all_keys.append(self.data_map[i][j][0])
    return all_keys
      
          
      
    
      
my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.print_table()

# print(my_hash_table.get_item('bolts'))
# print(my_hash_table.get_item('washers'))
# print(my_hash_table.get_item('lumber'))
# print(my_hash_table.get_item('cars'))
print(my_hash_table.keys())


