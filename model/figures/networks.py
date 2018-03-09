# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 10:36:23 2016

@author: srsampsa
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
plt.clf()
fig=plt.figure()

G1=nx.Graph()
G2=nx.Graph()
G3=nx.Graph()
sp = []
eu = []
sp_sizes = []
eu_sizes = []
for i in range(9):
    sp.append('sp'+str(i))
    sp_sizes.append(50)
    #sp_sizes.append(random.randint(1,50))
    #G1.add_node(sp[i])    
    G2.add_node(sp[i])
    G3.add_node(sp[i])
for i in range(9):
    eu.append('eu'+str(i))
    eu_sizes.append(50)
    #eu_sizes.append(random.randint(1,50))
    #G1.add_node(eu[i])
    G2.add_node(eu[i])
    G3.add_node(eu[i])


G1.add_node('pl1')
G1.add_node('pl2')

G2.add_node('pl1')

G3.add_node('pl1')
G3.add_node('pl2')

G1.add_node('sp0')
G1.add_edge('pl1','sp0')
G1.add_node('eu0')
G1.add_edge('pl1','eu0')

G1.add_node('sp1')
G1.add_edge('pl2','sp1')
G1.add_node('eu1')
G1.add_edge('pl2','eu1')


for i in range(len(sp)):
    G2.add_edge('pl1',sp[i])
    G2.add_edge('pl1',eu[i])
    
for i in range(0,int(len(sp)/2)):
    G3.add_edge('pl1',sp[i])
    G3.add_edge('pl1',eu[i])
for i in range(int(len(sp)/2),int(len(sp))):
    G3.add_edge('pl2',sp[i])
    G3.add_edge('pl2',eu[i])

G3.add_edge('pl1','pl2')

pos1=nx.spring_layout(G1)    
pos2=nx.spring_layout(G2)
pos3=nx.spring_layout(G3)



node_alpha=1
plt.subplot(234)
nx.draw_networkx_nodes(G1,pos1,nodelist=['pl1','pl2'],node_color='r',node_size=100,alpha=1)
nx.draw_networkx_nodes(G1,pos1,nodelist=['sp0','sp1'],node_color='k',node_size=sp_sizes,alpha=node_alpha)
nx.draw_networkx_nodes(G1,pos1,nodelist=['eu0','eu1'],node_color='w',node_size=eu_sizes,alpha=node_alpha)
nx.draw_networkx_edges(G1,pos1,width=1.0,alpha=0.3)
plt.axis('off')

plt.subplot(235)
nx.draw_networkx_nodes(G2,pos2,nodelist=['pl1'],node_color='r',node_size=100,alpha=1)
nx.draw_networkx_nodes(G2,pos2,nodelist=sp,node_color='k',node_size=sp_sizes,alpha=node_alpha)
nx.draw_networkx_nodes(G2,pos2,nodelist=eu,node_color='w',node_size=eu_sizes,alpha=node_alpha)
nx.draw_networkx_edges(G2,pos2,width=1.0,alpha=0.3)
plt.axis('off')

plt.subplot(236)
nx.draw_networkx_nodes(G3,pos3,nodelist=['pl1','pl2'],node_color='r',node_size=100,alpha=1)
nx.draw_networkx_nodes(G3,pos3,nodelist=sp,node_color='k',node_size=sp_sizes,alpha=node_alpha)
nx.draw_networkx_nodes(G3,pos3,nodelist=eu,node_color='w',node_size=eu_sizes,alpha=node_alpha)
nx.draw_networkx_edges(G3,pos3,width=1.0,alpha=0.3)
plt.axis('off')

fig.set_size_inches(12,5)
plt.savefig('fig1_networks.png') 
plt.show() # display

