# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:41:09 2018

Visualizing using Arc plots
Following on what you've learned about the nxviz API, now try making an ArcPlot 
of the network. Two keyword arguments that you will try here are 
node_order='keyX' and node_color='keyX', in which you specify a key in the node 
metadata dictionary to color and order the nodes by.

matplotlib.pyplot has been imported for you as plt.

INSTRUCTIONS
100 XP

Import ArcPlot from nxviz.

Create an un-customized ArcPlot of T. To do this, use the ArcPlot() function 
with just T as the argument.

Create another ArcPlot of T in which the nodes are ordered and colored by the 
'category' keyword. You'll have to specify the node_order and node_color 
parameters to do this. For both plots, be sure to draw them to the screen and 
display them with plt.show().

"""

# Import necessary modules
import networkx as nx

#This step performed for you on DataCamp...
#Data path
path="E:/DataCamp/22_Network_Analysis_in_Python_Part_1/Data/ego-twitter.p"

T = nx.read_gpickle(path)
print( "The Twitter network has been loaded as T.")

# Import necessary modules
import matplotlib.pyplot as plt
____

# Create the un-customized ArcPlot object: a
a = ____

# Draw a to the screen
____

# Display the plot
plt.show()

# Create the customized ArcPlot object: a2
a2 = ____

# Draw a2 to the screen
____

# Display the plot
plt.show()