# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:31:48 2018

Finding nodes involved in triangles
NetworkX provides an API for counting the number of triangles that every node 
is involved in: nx.triangles(G). It returns a dictionary of nodes as the keys 
and number of triangles as the values. Your job in this exercise is to modify 
the function defined earlier to extract all of the nodes involved in a 
triangle relationship with a given node.

INSTRUCTIONS
100 XP
Write a function nodes_in_triangle() that has two parameters - G and n - and 
identifies all nodes in a triangle relationship with a given node.

In the for loop, iterate over all possible triangle relationship combinations.

Check whether the nodes n1 and n2 have an edge between them. If they do, 
add both nodes to the set triangle_nodes.

Use your function in an assert statement to check that the number of nodes 
involved in a triangle relationship with node 1 of graph T is equal to 35.

"""
# Import necessary modules
import networkx as nx

#This step performed for you on DataCamp...
#Data path
path="E:/DataCamp/22_Network_Analysis_in_Python_Part_1/Data/ego-twitter.p"

T = nx.read_gpickle(path)
T = T.subgraph(list(range(0,50)))
T=T.to_undirected()
print( "A subsampled version of the Twitter network has been loaded as T.")
print("T has been converted to an undirected graph.")


from itertools import combinations

# Write a function that identifies all nodes in a triangle relationship with a given node.
def nodes_in_triangle(G, n):
    """
    Returns the nodes in a graph `G` that are involved in a triangle relationship with the node `n`.
    """
    triangle_nodes = set([n])
    
    # Iterate over all possible triangle relationship combinations
    for n1, n2 in ____:
    
        # Check if n1 and n2 have an edge between them
        if ____:
        
            # Add n1 to triangle_nodes
            ____
            
            # Add n2 to triangle_nodes
            ____
            
    return triangle_nodes
    
# Write the assertion statement
assert len(____(____, ____)) == ____