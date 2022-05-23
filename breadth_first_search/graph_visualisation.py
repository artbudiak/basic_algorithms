# libraries
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
 
# Build a dataframe with 4 connections
df = pd.DataFrame({ 'from':['YOU', 'Anuj', 'Thom', 'YOU', 'YOU', 'Alice', 'Claire', 'Bob', 'Alice'], 
                    'to':['Alice', 'Bob','Claire', 'Bob', 'Claire', 'Peggy', 'Jonny', 'Peggy', 'Peggy']})
 
# Build your graph
G=nx.from_pandas_edgelist(df, 'from', 'to')
 
# Plot it
nx.draw(G, with_labels=True, node_size = 1500, node_color = "green", alpha = 0.9)
plt.show()
