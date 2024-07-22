# ex pentagon graph

# A has edges with B and E
# B has edges with A and C
# C has edges with B and D
# D has edges with C and E
# E has edges with A and D


# Adjacency Matrix (AM):

#    A  B  C  D  E
# A  0  1  0  0  1
# B  1  0  1  0  1
# C  0  1  0  1  0
# D  0  0  1  0  1
# E  1  0  0  1  0

# Adjacency List (AL):
{
  'A': ['B', 'E'], 
  'B': ['A', 'C'],
  'C': ['B', 'D'],
  'D': ['C', 'E'],
  'E': ['A', 'D']
}

# The difference between AM and AL is that AM still has to store all verticies its not connected to with zeros.
# So for a space complexity stand point:
#  AM is o(|V|^2) - the number of vertices squared
#  AL is o(|V| + |E|) - the number of vertices + number of edges

# Big O for common operations with a graph:

#Adding a vertex F before adding edges:
#  AL its o(1)
#  AM its o(|V|^2) - need to add a new row and col and fill them with zeros

#Adding edges between B and F:
#  AL its o(1)
#  AM its o(1)

#Removing the vertex F:
#  AL its o(|V| + |E|) bc will need to remove all edges connected to F in the list
#  AM its o(|V|^2) bc will need to remove the extra row and col its rewriting the entire matrix

# problem with AM that it stores all the zeros if you have a company like fb you will have 1 billion verticies. 
# Even if you have 1000 friends you will be storing a million zeros for every 1 vertex.
# AM is very ineffiecient for a storage perspective compared to AL




 