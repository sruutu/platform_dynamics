# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.ticker as mtick
import matplotlib as mpl

mpl.rc('font',family='Arial')

dt= ''

hfont = {'fontname':'Arial'}

mydpi = 1000

#https://www.elsevier.com/authors/author-schemas/artwork-and-media-instructions/artwork-sizing
w_single = 90 / 25.4
h_single = w_single

w_double = 190 / 25.4
h_double = w_double * 0.5

xlabelsize= 8
legendsize = 10
titlesize = 10
titlesize_small = 8

### FIGURE 5 ###

fig5_scen1 = pd.read_csv('fig5_scen1.tab',sep='\t')
fig5_scen2 = pd.read_csv('fig5_scen2.tab',sep='\t')
fig5_scen3 = pd.read_csv('fig5_scen3.tab',sep='\t')

plt.figure()

ax1= plt.subplot(231)
plt.plot(fig5_scen1['Time'],fig5_scen1['Adopter Fraction[eu,p1]'],color='0',linewidth=2,label='Platform 1')
plt.plot(fig5_scen1['Time'],fig5_scen1['Adopter Fraction[eu,p2]'],'--',color='red',linewidth=2,label='Platform 2')
plt.xlim([0,15])
plt.ylim([0,0.01])
plt.ylabel('Adopter fraction\n(end users)', **hfont,fontsize=12)
plt.title('Scenario 1:\nFragmented development', **hfont,fontsize=titlesize)
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

ax2= plt.subplot(232)
plt.plot(fig5_scen2['Time'],fig5_scen2['Adopter Fraction[eu,p1]'],color='0',linewidth=2,label='Platform 1')
plt.plot(fig5_scen2['Time'],fig5_scen2['Adopter Fraction[eu,p2]'],'--',color='red',linewidth=2,label='Platform 2')
plt.xlim([0,15])
plt.ylim([0,0.1])
plt.title('Scenario 2:\nWinner-take-all', **hfont,fontsize=titlesize)
plt.setp(ax2.get_xticklabels(), visible=False)
                                                      
#ax.set_xticks([0,10,20,30], minor=True)                                           
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left') 

ax2.set_xticks([0,15])                                                                                                 
ax2.set_yticks([0,0.1])                                                       
#ax2.set_yticks([0,0.2,0.4,0.6,0.8,1], minor=True) 

ax3= plt.subplot(233)
plt.plot(fig5_scen3['Time'],fig5_scen3['Adopter Fraction[eu,p1]'],color='0',linewidth=2,label='Platform 1')
plt.plot(fig5_scen3['Time'],fig5_scen3['Adopter Fraction[eu,p2]'],'--',color='red',linewidth=2,label='Platform 2')
plt.xlim([0,15])
plt.ylim([0,0.8])
plt.title('Scenario 3:\nCollaboration and competition', **hfont,fontsize=titlesize)
plt.setp(ax3.get_xticklabels(), visible=False)
         

ax3.set_xticks([0,15])                                              
#ax.set_xticks([0,10,20,30], minor=True)                                           
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
ax3.xaxis.set_ticks_position('bottom')
ax3.yaxis.set_ticks_position('left') 
                                                                                                 
ax3.set_yticks([0,0.8])                                                       
#ax3.set_yticks([0,0.2,0.4,0.6,0.8,1], minor=True) 

ax4= plt.subplot(234)
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

ax5= plt.subplot(235)
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

ax6= plt.subplot(236)
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

fig = plt.gcf()
fig.set_size_inches(w_double,h_double)
plt.savefig('fig5'+dt+'.jpg',dpi=mydpi) 


### FIGURE 4 ###

fig4_05_4 = pd.read_csv('fig4_05_4.tab',sep='\t')
fig4_05_6= pd.read_csv('fig4_05_6.tab',sep='\t')
#fig4_075_3 = pd.read_csv('fig4_075_3.tab',sep='\t')
fig4_075_4 = pd.read_csv('fig4_075_4.tab',sep='\t')
fig4_075_6 = pd.read_csv('fig4_075_6.tab',sep='\t')


fig, ax = plt.subplots()

plt.plot(fig4_05_4['Time'],fig4_05_4['Combined adopter fraction[eu]'],'--',color='red',linewidth=1,label=r'$\tau=0.5,  T=4$')
plt.plot(fig4_05_6['Time'],fig4_05_6['Combined adopter fraction[eu]'],'-',color='red',linewidth=2,label=r'$\tau=0.5,  T=6$')
#plt.plot(fig4_075_3['Time'],fig4_075_3['Combined adopter fraction[eu]'],'--',color='k',linewidth=1,label=r'$\tau=0.75, T=3$')
plt.plot(fig4_075_4['Time'],fig4_075_4['Combined adopter fraction[eu]'],'--',color='k',linewidth=1,label=r'$\tau=0.75, T=4$')
plt.plot(fig4_075_6['Time'],fig4_075_6['Combined adopter fraction[eu]'],'-',color='k',linewidth=2,label=r'$\tau=0.75, T=6$')

#plt.ylabel('Adopter fraction (end users, both platforms)', **hfont)
plt.xlabel('Time', **hfont,fontsize=xlabelsize)


y1=fig4_05_4['Combined adopter fraction[eu]']
y2=fig4_05_6['Combined adopter fraction[eu]']
ax.fill_between(fig4_05_4['Time'],y1, y2, where=y2 >= y1, facecolor='red', interpolate=True, alpha=0.1)

y1=fig4_075_4['Combined adopter fraction[eu]']
y2=fig4_075_6['Combined adopter fraction[eu]']
ax.fill_between(fig4_05_4['Time'],y1, y2, where=y2 >= y1, facecolor='black', interpolate=True, alpha=0.1)

plt.ylim([0,0.1])
plt.xlim([0,10])

ax.set_xticks([0,10])                                                       
#ax.set_xticks([0,10,20,30], minor=True)                                           
ax.set_yticks([0,0.1])                                                       
#ax.set_yticks([0,0.2,0.4,0.6,0.8,1], minor=True) 
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
#ax.spines['left'].set_visible(False)  
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

box = ax.get_position()
ax.set_position([box.x0, box.y0+ box.height * 0.2, box.width, box.height*0.8])
#ax.legend(loc=0,framealpha=0,fontsize=10)
ax.legend(loc='upper center', bbox_to_anchor=(0.5,-0.15), ncol=2,framealpha=0,fontsize=legendsize)

plt.suptitle('Adopter fraction', **hfont,fontsize=titlesize)
plt.title('(end users, both platforms)', **hfont,fontsize=titlesize_small)

fig = plt.gcf()
fig.set_size_inches(w_single,h_single)
plt.savefig('fig4'+dt+'.jpg',dpi=mydpi) 


### FIGURE 6 ###

fig6_05_4 = pd.read_csv('fig6_05_4.tab',sep='\t')
fig6_05_6= pd.read_csv('fig6_05_6.tab',sep='\t')
#fig6_075_3 = pd.read_csv('fig6_075_3.tab',sep='\t')
fig6_075_4 = pd.read_csv('fig6_075_4.tab',sep='\t')
fig6_075_6 = pd.read_csv('fig6_075_6.tab',sep='\t')

fig,ax = plt.subplots()

plt.plot(fig6_05_4['Time'],fig6_05_4['Combined adopter fraction[eu]'],'--',color='red',linewidth=1,label=r'$\tau=0.5,  T=4$')
plt.plot(fig6_05_6['Time'],fig6_05_6['Combined adopter fraction[eu]'],'-',color='red',linewidth=2,label=r'$\tau=0.5,  T=6$')
#plt.plot(fig6_075_3['Time'],fig6_075_3['Combined adopter fraction[eu]'],'--',color='k',linewidth=1,label=r'$\tau=0.75, T=3$')
plt.plot(fig6_075_4['Time'],fig6_075_4['Combined adopter fraction[eu]'],'--',color='k',linewidth=1,label=r'$\tau=0.75, T=4$')
plt.plot(fig6_075_6['Time'],fig6_075_6['Combined adopter fraction[eu]'],'-',color='k',linewidth=2,label=r'$\tau=0.75, T=6$')
plt.legend(loc=0,framealpha=0,fontsize=legendsize)

y1=fig6_05_4['Combined adopter fraction[eu]']
y2=fig6_05_6['Combined adopter fraction[eu]']
ax.fill_between(fig6_05_4['Time'],y1, y2, where=y2 >= y1, facecolor='red', interpolate=True, alpha=0.1)

y1=fig6_075_4['Combined adopter fraction[eu]']
y2=fig6_075_6['Combined adopter fraction[eu]']
ax.fill_between(fig6_05_4['Time'],y1, y2, where=y2 >= y1, facecolor='black', interpolate=True, alpha=0.1)

plt.xlabel('Time', **hfont,fontsize=xlabelsize)
#plt.ylabel('Adopter fraction (end users, both platforms)', **hfont)
plt.ylim([0,0.1])
plt.xlim([0,10])

ax.set_xticks([0,10])                                                       
#ax.set_xticks([0,10,20,30], minor=True)                                           
ax.set_yticks([0,0.1])                                                       
#ax.set_yticks([0,0.2,0.4,0.6,0.8,1], minor=True) 
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
#ax.spines['left'].set_visible(False)  
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

box = ax.get_position()
ax.set_position([box.x0, box.y0+ box.height * 0.2, box.width, box.height*0.8])
#ax.legend(loc=0,framealpha=0,fontsize=10)
ax.legend(loc='upper center', bbox_to_anchor=(0.5,-0.15), ncol=2,framealpha=0,fontsize=legendsize)

plt.suptitle('Adopter fraction', **hfont,fontsize=titlesize)
plt.title('(end users, both platforms)', **hfont,fontsize=titlesize_small)

fig = plt.gcf()
fig.set_size_inches(w_single,h_single)
plt.savefig('fig6'+dt+'.jpg',dpi=mydpi) 


### FIGURE 8 ###

fig8_theta0 = pd.read_csv('fig8_theta0.tab',sep='\t')
fig8_theta05 = pd.read_csv('fig8_theta05.tab',sep='\t')
fig8_theta1 = pd.read_csv('fig8_theta1.tab',sep='\t')


plt.figure()
ax=plt.subplot(211)
plt.plot(fig8_theta0['Time'],fig8_theta0['Adopter Fraction[eu,p1]'],color='0',linewidth=2,label=r'$\theta=0$')
plt.plot(fig8_theta05['Time'],fig8_theta05['Adopter Fraction[eu,p1]'],color='0',linewidth=1,label=r'$\theta=0.5$')
plt.plot(fig8_theta1['Time'],fig8_theta1['Adopter Fraction[eu,p1]'],'--',color='0',linewidth=1,label=r'$\theta=1$')
#plt.ylabel('Adopter fraction (platform 1)', **hfont)
plt.title('(end users, platform 1)', **hfont,fontsize=titlesize_small)
#plt.legend(loc=4,ncol=2,framealpha=0)
plt.setp(ax.get_xticklabels(), visible=False)

ax.set_xticks([0,30])                                                       
#ax.set_xticks([0,10,20,30], minor=True)                                           
ax.set_yticks([0,1])                                                       
#ax.set_yticks([0,0.2,0.4,0.6,0.8,1], minor=True)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left') 
plt.setp(ax1.get_xticklabels(), visible=False)

box = ax.get_position()
ax.set_position([box.x0, box.y0+ box.height * 0.2, box.width, box.height*0.8])
#plt.xlabel('Time', **hfont,fontsize=12)
plt.xlabel('Time', **hfont,fontsize=xlabelsize)

ax=plt.subplot(212)
plt.plot(fig8_theta0['Time'],fig8_theta0['Adopter Fraction[sp,p1]'],color='0',linewidth=2,label=r'$\theta=0$')
plt.plot(fig8_theta05['Time'],fig8_theta05['Adopter Fraction[sp,p1]'],color='0',linewidth=1,label=r'$\theta=0.5$')
plt.plot(fig8_theta1['Time'],fig8_theta1['Adopter Fraction[sp,p1]'],'--',color='0',linewidth=1,label=r'$\theta=1$')
#plt.ylabel('Adopter fraction', **hfont)
plt.title('(service providers, platform 1)', **hfont,fontsize=titlesize_small)
#plt.legend(loc=0,ncol=1,framealpha=0)
plt.xlabel('Time', **hfont,fontsize=xlabelsize)
plt.ylim([0,1])

ax.set_xticks([0,30])                                                       
#ax.set_xticks([0,10,20,30], minor=True)                                           
ax.set_yticks([0,1])                                                       
#ax.set_yticks([0,0.2,0.4,0.6,0.8,1], minor=True)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
#ax.spines['left'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left') 

box = ax.get_position()
ax.set_position([box.x0, box.y0+ box.height * 0.2, box.width, box.height*0.8])
                 
# Put a legend below current axis
ax.legend(loc='upper center', bbox_to_anchor=(0.5,-0.3), ncol=3,framealpha=0,fontsize=legendsize)

#labels = [item.get_text() for item in ax.get_yticklabels()]
#empty_string_labels = ['']*len(labels)
#ax.set_yticklabels(empty_string_labels)

plt.suptitle('Adopter fraction', **hfont,fontsize=titlesize)

fig = plt.gcf()
fig.set_size_inches(w_single,h_single)
plt.savefig('fig8'+dt+'.jpg',dpi=mydpi) 



### FIGURE 9 ###

fig9_theta0 = pd.read_csv('fig9_theta0.tab',sep='\t')
fig9_theta05 = pd.read_csv('fig9_theta05.tab',sep='\t')
fig9_theta1 = pd.read_csv('fig9_theta1.tab',sep='\t')

plt.figure()

ax=plt.subplot(211)
plt.plot(fig9_theta0['Time'],fig9_theta0['Adopter Fraction[eu,p1]'],color='0',linewidth=2,label='Platform 1')
plt.plot(fig9_theta0['Time'],fig9_theta0['Adopter Fraction[eu,p2]'],'--',color='red',linewidth=1,label='Platform 2')
#plt.ylabel('Adopter fraction (end users)', **hfont)
plt.title(r'$\theta=0$', **hfont,fontsize=titlesize)
#plt.legend(loc=0,ncol=1,framealpha=0)
#plt.xlabel('Time', **hfont,fontsize=12)
plt.ylim([0,1])
plt.setp(ax.get_xticklabels(), visible=False)

ax.set_xticks([0,30])                                                       
#ax.set_xticks([0,10,20,30], minor=True)                                           
ax.set_yticks([0,1])                                                       
#ax.set_yticks([0,0.2,0.4,0.6,0.8,1], minor=True)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left') 

box = ax.get_position()
ax.set_position([box.x0, box.y0+ box.height * 0.2, box.width, box.height*0.8])
plt.xlabel('Time', **hfont,fontsize=xlabelsize)

ax=plt.subplot(212)
plt.plot(fig9_theta05['Time'],fig9_theta05['Adopter Fraction[eu,p1]'],color='0',linewidth=2,label='Platform 1')
plt.plot(fig9_theta05['Time'],fig9_theta05['Adopter Fraction[eu,p2]'],'--',color='red',linewidth=1,label='Platform 2')
#plt.ylabel('End user adopter fraction', **hfont)
plt.title(r'$\theta=0.5$', **hfont,fontsize=titlesize)
#plt.legend(loc=0,ncol=1,framealpha=0)
plt.xlabel('Time', **hfont,fontsize=xlabelsize)
plt.ylim([0,1])

#labels = [item.get_text() for item in ax.get_yticklabels()]
#empty_string_labels = ['']*len(labels)
#ax.set_yticklabels(empty_string_labels)

ax.set_xticks([0,30])                                                       
#ax.set_xticks([0,10,20,30], minor=True)                                           
ax.set_yticks([0,1])                                                       
#ax.set_yticks([0,0.2,0.4,0.6,0.8,1], minor=True) 
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
#ax.spines['left'].set_visible(False)  
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

box = ax.get_position()
ax.set_position([box.x0, box.y0+ box.height * 0.2, box.width, box.height*0.8])

ax.legend(loc='upper center', bbox_to_anchor=(0.5,-0.3), ncol=2,framealpha=0,fontsize=legendsize)


plt.suptitle('Adopter fraction (end users)', **hfont,fontsize=titlesize)

fig = plt.gcf()
fig.set_size_inches(w_single,h_single)
plt.savefig('fig9'+dt+'.jpg',dpi=mydpi) 

### FIGURE 10 ###

fig10_theta0 = pd.read_csv('fig10_theta0.tab',sep='\t')
fig10_theta05 = pd.read_csv('fig10_theta05.tab',sep='\t')
fig10_theta1 = pd.read_csv('fig10_theta1.tab',sep='\t')

plt.figure()

ax=plt.subplot(211)
plt.plot(fig10_theta0['Time'],fig10_theta0['Adopter Fraction[eu,p1]'],color='0',linewidth=2,label='Platform 1')
plt.plot(fig10_theta0['Time'],fig10_theta0['Adopter Fraction[eu,p2]'],'--',color='red',linewidth=1,label='Platform 2')
#plt.ylabel('Adopter fraction (end users)', **hfont)
plt.title(r'$\theta=0$', **hfont,fontsize=titlesize)
#plt.legend(loc=0,ncol=1,framealpha=0)
#plt.xlabel('Time', **hfont,fontsize=12)
plt.ylim([0,1])
plt.setp(ax.get_xticklabels(), visible=False)
plt.xlabel('Time', **hfont,fontsize=xlabelsize)

#labels = [item.get_text() for item in ax.get_xticklabels()]
#empty_string_labels = ['']*len(labels)
#ax.set_xticklabels(empty_string_labels)
                       
ax.set_xticks([0,30])                                                       
#ax.set_xticks([0,10,20,30], minor=True)                                           
ax.set_yticks([0,1])                                                       
#ax.set_yticks([0,0.2,0.4,0.6,0.8,1], minor=True) 
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False) 
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

box = ax.get_position()
ax.set_position([box.x0, box.y0+ box.height * 0.2, box.width, box.height*0.8])

ax = plt.subplot(212)
plt.plot(fig10_theta05['Time'],fig10_theta05['Adopter Fraction[eu,p1]'],color='0',linewidth=2,label='Platform 1')
plt.plot(fig10_theta05['Time'],fig10_theta05['Adopter Fraction[eu,p2]'],'--',color='red',linewidth=1,label='Platform 2')
#plt.ylabel('End user adopter fraction', **hfont)
plt.title(r'$\theta=0.5$', **hfont,fontsize=titlesize)
#plt.legend(loc=0,ncol=1,framealpha=0)
plt.xlabel('Time', **hfont,fontsize=xlabelsize)
plt.ylim([0,1])


ax.set_xticks([0,30])                                                       
#ax.set_xticks([0,10,20,30], minor=True)                                           
ax.set_yticks([0,1])                                                       
#ax.set_yticks([0,0.2,0.4,0.6,0.8,1], minor=True)
ax.spines['right'].set_visible(False) 
ax.spines['top'].set_visible(False)
#ax.spines['left'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left') 

box = ax.get_position()
ax.set_position([box.x0, box.y0+ box.height * 0.2, box.width, box.height*0.8])

ax.legend(loc='upper center', bbox_to_anchor=(0.5,-0.3), ncol=2,framealpha=0,fontsize=legendsize)


plt.suptitle('Adopter fraction (end users)', **hfont,fontsize=titlesize)

fig = plt.gcf()
fig.set_size_inches(w_single,h_single)
plt.savefig('fig10.jpg', dpi=mydpi) 

