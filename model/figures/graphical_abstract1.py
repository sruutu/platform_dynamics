# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 13:43:04 2016

@author: srsampsa
"""

import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.ticker as mtick
import matplotlib as mpl

mpl.rc('font',family='Arial')

dt= ''

hfont = {'fontname':'Arial'}

mydpi = 100

#https://www.elsevier.com/authors/author-schemas/artwork-and-media-instructions/artwork-sizing

height = 5.31
ratio = 1328/531
#width = height*ratio
width = 13.28

xlabelsize= 8
legendsize = 10
titlesize = 10
titlesize_small = 8

### FIGURE 5 ###

fig5_scen1 = pd.read_csv('fig5_scen1.tab',sep='\t')
fig5_scen2 = pd.read_csv('fig5_scen2.tab',sep='\t')
fig5_scen3 = pd.read_csv('fig5_scen3.tab',sep='\t')

plt.figure()

ax1= plt.subplot(334)
plt.plot(fig5_scen1['Time'],fig5_scen1['Adopter Fraction[eu,p1]'],color='0',linewidth=2,label='Platform 1')
plt.plot(fig5_scen1['Time'],fig5_scen1['Adopter Fraction[eu,p2]'],'--',color='red',linewidth=2,label='Platform 2')
plt.xlim([0,15])
plt.ylim([0,0.01])
plt.ylabel('Adopter fraction\n(end users)', **hfont,fontsize=12)
#plt.title('Scenario 1:\nFragmented development', **hfont,fontsize=titlesize)
plt.legend(loc=0,ncol=1,framealpha=0,fontsize=legendsize)
plt.setp(ax1.get_xticklabels(), visible=False)
                                             
#ax.set_xticks([0,10,20,30], minor=True)                                           
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left') 

ax1.set_xticks([0,15])                                                                                                 
ax1.set_yticks([0,0.01])                                                       
#ax1.set_yticks([0,0.2,0.4,0.6,0.8,1], minor=True) 

ax2= plt.subplot(335)
plt.plot(fig5_scen2['Time'],fig5_scen2['Adopter Fraction[eu,p1]'],color='0',linewidth=2,label='Platform 1')
plt.plot(fig5_scen2['Time'],fig5_scen2['Adopter Fraction[eu,p2]'],'--',color='red',linewidth=2,label='Platform 2')
plt.xlim([0,15])
plt.ylim([0,0.1])
#plt.title('Scenario 2:\nWinner-take-all', **hfont,fontsize=titlesize)
plt.setp(ax2.get_xticklabels(), visible=False)
                                                      
#ax.set_xticks([0,10,20,30], minor=True)                                           
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left') 

ax2.set_xticks([0,15])                                                                                                 
ax2.set_yticks([0,0.1])                                                       
#ax2.set_yticks([0,0.2,0.4,0.6,0.8,1], minor=True) 

ax3= plt.subplot(336)
plt.plot(fig5_scen3['Time'],fig5_scen3['Adopter Fraction[eu,p1]'],color='0',linewidth=2,label='Platform 1')
plt.plot(fig5_scen3['Time'],fig5_scen3['Adopter Fraction[eu,p2]'],'--',color='red',linewidth=2,label='Platform 2')
plt.xlim([0,15])
plt.ylim([0,0.8])
#plt.title('Scenario 3:\nCollaboration and competition', **hfont,fontsize=titlesize)
plt.setp(ax3.get_xticklabels(), visible=False)
         

ax3.set_xticks([0,15])                                              
#ax.set_xticks([0,10,20,30], minor=True)                                           
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
ax3.xaxis.set_ticks_position('bottom')
ax3.yaxis.set_ticks_position('left') 
                                                                                                 
ax3.set_yticks([0,0.8])                                                       
#ax3.set_yticks([0,0.2,0.4,0.6,0.8,1], minor=True) 

ax4= plt.subplot(337)
plt.semilogy(fig5_scen1['Time'],fig5_scen1['Quality[p1]'],color='0',linewidth=2,label='Platform 1')
plt.semilogy(fig5_scen1['Time'],fig5_scen1['Quality[p2]'],'--',color='red',linewidth=2,label='Platform 2')
plt.xlim([0,15])
plt.ylim([0,10000])
plt.ylabel('\nPlatform quality', **hfont,fontsize=12)
plt.xlabel('Time', **hfont,fontsize=xlabelsize)

ax4.set_xticks([0,15])                                                       
#ax.set_xticks([0,10,20,30], minor=True)                                           
ax4.spines['right'].set_visible(False)
ax4.spines['top'].set_visible(False)
ax4.xaxis.set_ticks_position('bottom')
ax4.yaxis.set_ticks_position('left') 

ax5= plt.subplot(338)
plt.semilogy(fig5_scen2['Time'],fig5_scen2['Quality[p1]'],color='0',linewidth=2,label='Platform 1')
plt.semilogy(fig5_scen2['Time'],fig5_scen2['Quality[p2]'],'--',color='red',linewidth=2,label='Platform 2')
plt.xlim([0,15])
plt.ylim([0,10000])
plt.xlabel('Time', **hfont,fontsize=xlabelsize)

ax5.set_xticks([0,15])                                                       
#ax.set_xticks([0,10,20,30], minor=True)                                           
ax5.spines['right'].set_visible(False)
ax5.spines['top'].set_visible(False)
ax5.xaxis.set_ticks_position('bottom')
ax5.yaxis.set_ticks_position('left') 

ax6= plt.subplot(339)
plt.semilogy(fig5_scen3['Time'],fig5_scen3['Quality[p1]'],color='0',linewidth=2,label='Platform 1')
plt.semilogy(fig5_scen3['Time'],fig5_scen3['Quality[p2]'],'--',color='red',linewidth=2,label='Platform 2')
plt.xlim([0,15])
plt.ylim([0,10000])
plt.xlabel('Time', **hfont,fontsize=xlabelsize)

ax6.set_xticks([0,15])                                                       
#ax.set_xticks([0,10,20,30], minor=True)                                           
ax6.spines['right'].set_visible(False)
ax6.spines['top'].set_visible(False)
ax6.xaxis.set_ticks_position('bottom')
ax6.yaxis.set_ticks_position('left') 




node_alpha=1
plt.subplot(331)
nx.draw_networkx_nodes(G1,pos1,nodelist=['pl1','pl2'],node_color='g',node_size=100,alpha=1)
nx.draw_networkx_nodes(G1,pos1,nodelist=['sp0','sp1'],node_color='k',node_size=sp_sizes,alpha=node_alpha)
nx.draw_networkx_nodes(G1,pos1,nodelist=['eu0','eu1'],node_color='w',node_size=eu_sizes,alpha=node_alpha)
nx.draw_networkx_edges(G1,pos1,width=1.0,alpha=0.3)
plt.axis('off')
plt.title('Scenario 1:\nFragmented development',**hfont,fontsize=titlesize)

plt.subplot(332)
nx.draw_networkx_nodes(G2,pos2,nodelist=['pl1'],node_color='g',node_size=100,alpha=1)
nx.draw_networkx_nodes(G2,pos2,nodelist=sp,node_color='k',node_size=sp_sizes,alpha=node_alpha)
nx.draw_networkx_nodes(G2,pos2,nodelist=eu,node_color='w',node_size=eu_sizes,alpha=node_alpha)
nx.draw_networkx_edges(G2,pos2,width=1.0,alpha=0.3)
plt.axis('off')
plt.title('Scenario 2:\nWinner-take-all',**hfont,fontsize=titlesize)

plt.subplot(333)
nx.draw_networkx_nodes(G3,pos3,nodelist=['pl1','pl2'],node_color='g',node_size=100,alpha=1)
nx.draw_networkx_nodes(G3,pos3,nodelist=sp,node_color='k',node_size=sp_sizes,alpha=node_alpha)
nx.draw_networkx_nodes(G3,pos3,nodelist=eu,node_color='w',node_size=eu_sizes,alpha=node_alpha)
nx.draw_networkx_edges(G3,pos3,width=1.0,alpha=0.3)
plt.axis('off')
plt.title('Scenario 3:\nCollaboration and competition',**hfont,fontsize=titlesize)



fig = plt.gcf()
fig.set_size_inches(width,height)
plt.savefig('graphical_abstract'+dt+'.jpg',dpi=mydpi) 