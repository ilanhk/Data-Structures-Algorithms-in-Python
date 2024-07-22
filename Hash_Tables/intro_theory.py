# you can store a dictionary {key: value} in a hash table. You need to pass it in a hash function it will store it and give you an address where its stored and the dict is stored as an array
# Hash is only one way - you can only put a key to get the address not address to get the key
# a Hash is "Deterministic" -means if we put ex {"nails": 200} in a hash function and gives us the address 3. It will always give us the address 3 everytime we put the key "nails"
# there is a way you can store multiple key: value pairs in the same address with out overwriting the other key: value pair s

# Collisions - happens when you put a key value pair at an address in the table where there was already one. If they are put together its called "Separate Chaining"
# Another popular way to deal with collisions is to go down the table til you find an empty address to put the key value pair there.
# if you have another key value pair you will continue to go down the table till you find another empty address to store it in this is called "Linear Probing" its a form of "open addressing"

# Another way to do "Separate Chaining" instead of having lists that are all stored at that address, we can have linked lists to store at the same address
