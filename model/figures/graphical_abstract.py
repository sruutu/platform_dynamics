# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:48:26 2016

@author: srsampsa
"""

import pandas as pd
import matplotlib.pyplot as plt
mydpi = 1000


fig5_scen1 = pd.read_csv('fig5_scen1.tab',sep='\t')
fig5_scen2 = pd.read_csv('fig5_scen2.tab',sep='\t')
fig5_scen3 = pd.read_csv('fig5_scen3.tab',sep='\t')

plt.figure()

ax1= plt.subplot(234)
plt.plot(fig5_scen1['Time'],fig5_scen1['Adopter Fraction[eu,p1]'],color='0',linewidth=3,label='Platform 1')
plt.plot(fig5_scen1['Time'],fig5_scen1['Adopter Fraction[eu,p2]'],'--',color='red',linewidth=3,label='Platform 2')
plt.xlim([0,8])
plt.ylim([-0.0,0.02])
#plt.ylabel('Adopter fraction\n(end users)')

#plt.legend(loc=0,ncol=1,framealpha=0)
plt.setp(ax1.get_xticklabels(), visible=False)

plt.gca().axison = False

ax1.set_xticks([0,8])                                                                                                 
ax1.set_yticks([-0,0.02])                                                       
plt.setp(ax1.get_yticklabels(), visible=False)


ax2= plt.subplot(235)
plt.plot(fig5_scen2['Time'],fig5_scen2['Adopter Fraction[eu,p1]'],color='0',linewidth=3,label='Platform 1')
plt.plot(fig5_scen2['Time'],fig5_scen2['Adopter Fraction[eu,p2]'],'--',color='red',linewidth=3,label='Platform 2')
plt.xlim([0,12])
plt.ylim([0,0.1])

plt.setp(ax2.get_xticklabels(), visible=False)

ax2.set_xticks([0,12])                                                                                                 
ax2.set_yticks([-0.00,0.1])  
plt.setp(ax2.get_yticklabels(), visible=False)                                                     
plt.gca().axison = False

ax3= plt.subplot(236)
plt.plot(fig5_scen3['Time'],fig5_scen3['Adopter Fraction[eu,p1]'],color='0',linewidth=3,label='Platform 1')
plt.plot(fig5_scen3['Time'],fig5_scen3['Adopter Fraction[eu,p2]'],'--',color='red',linewidth=3,label='Platform 2')
plt.xlim([0,12])
plt.ylim([0,1])

plt.setp(ax3.get_xticklabels(), visible=False)

ax3.set_xticks([0,12])                                                                                                 
ax3.set_yticks([0,1])                                                       

plt.setp(ax3.get_yticklabels(), visible=False)
plt.gca().axison = False

node_alpha=1
plt.subplot(231)
nx.draw_networkx_nodes(G1,pos1,nodelist=['pl1','pl2'],node_color='g',node_size=100,alpha=1)
nx.draw_networkx_nodes(G1,pos1,nodelist=['sp0','sp1'],node_color='k',node_size=sp_sizes,alpha=node_alpha)
nx.draw_networkx_nodes(G1,pos1,nodelist=['eu0','eu1'],node_color='w',node_size=eu_sizes,alpha=node_alpha)
nx.draw_networkx_edges(G1,pos1,width=1.0,alpha=0.3)
plt.axis('off')
plt.title('Fragmented\ndevelopment')

plt.subplot(232)
nx.draw_networkx_nodes(G2,pos2,nodelist=['pl1'],node_color='g',node_size=100,alpha=1)
nx.draw_networkx_nodes(G2,pos2,nodelist=sp,node_color='k',node_size=sp_sizes,alpha=node_alpha)
nx.draw_networkx_nodes(G2,pos2,nodelist=eu,node_color='w',node_size=eu_sizes,alpha=node_alpha)
nx.draw_networkx_edges(G2,pos2,width=1.0,alpha=0.3)
plt.axis('off')
plt.title('Winner-take-all')

plt.subplot(233)
nx.draw_networkx_nodes(G3,pos3,nodelist=['pl1','pl2'],node_color='g',node_size=100,alpha=1)
nx.draw_networkx_nodes(G3,pos3,nodelist=sp,node_color='k',node_size=sp_sizes,alpha=node_alpha)
nx.draw_networkx_nodes(G3,pos3,nodelist=eu,node_color='w',node_size=eu_sizes,alpha=node_alpha)
nx.draw_networkx_edges(G3,pos3,width=1.0,alpha=0.3)
plt.axis('off')
plt.title('Collaboration and\ncompetition')


fig = plt.gcf()
fig.set_size_inches(13,5)
plt.savefig('graphical_abstract.jpg',dpi=mydpi) 
