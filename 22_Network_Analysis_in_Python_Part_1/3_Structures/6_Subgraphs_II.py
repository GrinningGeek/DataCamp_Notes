# -*- coding: utf-8 -*-
"""
Subgraphs II
In the previous exercise, we gave you a list of nodes whose neighbors we 
asked you to extract.

Let's try one more exercise in which you extract nodes that have a particular 
metadata property and their neighbors. This should hark back to what you've 
learned about using list comprehensions to find nodes. The exercise will also
build your capacity to compose functions that you've already written before.


INSTRUCTIONS
100 XP

Using a list comprehension, extract nodes that have the metadata 'occupation' 
as 'celebrity' alongside their neighbors:
    
The output expression of the list comprehension is n, and there are two 
iterator variables: n and d. The iterable is the list of nodes of T 
(including the metadata, which you can specify using data=True) and the 
conditional expression is if the 'occupation' key of the metadata dictionary 
d equals 'celebrity'.

Place them in a new subgraph called T_sub. To do this:   
    
Iterate over the nodes, compute the neighbors of each node, and add them to 
the set of nodes nodeset by using the .union() method. This last part has 
been done for you.

Use nodeset along with the T.subgraph() method to calculate T_sub.

Draw T_sub to the screen.

THE DATACAMP SOLUTION IS DEPRICATED AND THROWS RUNTIME ERRORS IN THE REAL 
WORLD

"""
# Import necessary modules
import networkx as nx
import matplotlib as plt

#This step performed for you on DataCamp...
#Data path
path="E:/DataCamp/22_Network_Analysis_in_Python_Part_1/Data/ego-twitter.p"

T = nx.read_gpickle(path)
T=T.to_undirected()
print( "The Twitter network has been loaded as T.")
print("T has been converted to an undirected graph.")

# Extract the nodes of interest: nodes
nodes = [n for n, d in ____ if ____ == ____]

# Create the set of nodes: nodeset
nodeset = set(nodes)

# Iterate over nodes
for n in ____:

    # Compute the neighbors of n: nbrs
    nbrs = ____
    
    # Compute the union of nodeset and nbrs: nodeset
    nodeset = nodeset.union(nbrs)

# Compute the subgraph using nodeset: T_sub
T_sub = ____

# Draw T_sub to the screen
____
plt.show()