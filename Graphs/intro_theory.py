#  a node in a graph is called a "vertex"(correct way to say) or a "node" (vertices for multiple)
# between a the vertices is called and "edge"(correct way to say) or a "connection"
# lets say you have vertices A,B,C it can be this structure A - B - C -A (triangle shape)
# There is no limit to how many vertices a vertex can connect to.

# lets say if you have a triangle graph you want to go B to C either you can go B to C or B to A than to C.
# you want to go the fastest route B to C but "weighted edges" will might say that it will take longer if you do B to C than B to A than C.(this is used in google map or waze to aviod traffic or networking routing protocols).
# edges can be weighted or not weighted.
# another concept with graphs a facebook connection between me and a friend is "bidirectional"(both ways) but Instagram or twitter between me and someone a celebraty its one way "directional" I am following them but they are not following me back.
# edges weighted or non weighted it can be directional or bidirectional

# trees are a form of graphs - but the limitation is that each node can only point to two other nodes
# since linked lists can be a form of a tree its also a form of a graph

# Two ways to look at graphs one is Adjacency Matrix other is Adjacency list 



# Graphs: Adjacency Matrix 
# ex vertices connected in a pentagon shape

# the vertical letters represent vertices
# the horizontal letters represents the vertices its edged with
# 0 is no edge 1 is edge
# if the edges are weighted it will be represented with whatever weighted number it has like 5 or 40 instead of one



#    A  B  C  D  E
# A  0  1  0  0  1
# B  1  0  1  0  1
# C  0  1  0  1  0
# D  0  0  1  0  1
# E  1  0  0  1  0


# A has edges with B and E
# B has edges with A and C
# C has edges with B and D
# D has edges with C and E
# E has edges with A and D

# obviously A cant connect to A and B connect to B etc.. so you will always see a 45 degree line of zeros and a symetry of 1s in between it. This happens if its only bidirectional.
# if its just directional connection the symetry will be lost



# Graphs: Adjacency List 
# ex vertices connected in a pentagon shape (same as the Adjacency Matrix ex)

{
  'A': ['B', 'E'], # A has edges with B and E
  'B': ['A', 'C'],
  'C': ['B', 'D'],
  'D': ['C', 'E'],
  'E': ['A', 'D']
}


