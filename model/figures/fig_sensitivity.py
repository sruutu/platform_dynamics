# -*- coding: utf-8 -*-
"""
Created on Wed May 25 15:20:49 2016

@author: srsampsa
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import warnings
warnings.simplefilter(action = "ignore", category = RuntimeWarning)

import matplotlib as mpl
mpl.rc('font',family='Arial')

hfont = {'fontname':'Arial'}

tolerance = 0.000001
#tolerance =  0.001
        
dt= ''        
        
def diff(x,tolerance):
    diff=[]
    for i in range(1,len(x)):
        if abs(x[i] - x[i-1])>tolerance:
            diff.append(x[i] - x[i-1])
        else:
            diff.append(0)
    return diff
    
def length(x):
    lengthi=0
    for i in range(1,len(x)):
        lengthi = lengthi + abs(x[i] - x[i-1])
    return lengthi

def luok(x):
    first_der = ''
    last = ''
    previous = ''
    d = diff(x,tolerance)
        
    for i in range(start,len(x)-1): # aloitetaan aikahetkeltä T1
        if last == '':
            if d[i] > 0:
                first_der = first_der + '+'
                last = '+'
            elif d[i] < 0:
                first_der = first_der + '-'
                last = '-'
            else:
                first_der = first_der + '0'
                last = '0'
        elif last == '+':
            if d[i] < 0:
                first_der = first_der + '-'
                last = '-'
            elif d[i] == 0:
                last = '0'
                previous = '+'
        elif last == '-':
            if d[i] > 0:
                first_der = first_der + '+'
                last = '+'
            elif d[i] == 0:
                last = '0'
                previous = '-'
        elif last == '0':
            if d[i] > 0 and not previous=='+':
                first_der = first_der + '0+'
                last = '+'
            elif d[i] < 0 and not previous=='-':
                first_der = first_der + '0-'  
                last = '-'
            else:
                if d[i] < 0:
                    last = '-'
                if d[i] > 0:
                    last = '+'
                    
    return first_der

def select(data,params,tyyppi):
    xx=[]
    xx2=[]
    pp =[]
    var_name = 'Combined adopter fraction[eu]'
    var_name2 = 'Combined adopter fraction[sp]'

    for i in range(1,sims+1):
        col = 'S'+str(i)+' '+var_name
        col2 = 'S'+str(i)+' '+var_name2
        if tyyppi == 'collapse':
            criteria = data[col][len(data[col])-1] < 0.001  and luok(data[col]) != '-'
        else:
            criteria = data[col][len(data[col])-1] > 0.1 and luok(data[col]) != '+'
        #print(luok(data[col]))
        if criteria:
            xx.append(data[col])
            xx.append(data[col2])
            p = []
            p.append(i)
            for j in range(len(params)):
                if 'SWITCH' in params[j]:
                    if data['S' + str(i)+ ' ' + params[j]][0] > 0.5:
                        p.append(1)
                    else:
                        p.append(0)
                else:
                    p.append(data['S' + str(i)+ ' ' + params[j]][0])
            p.append(luok(data[col]))
            p.append(luok(data[col2]))
            
            pp.append(p)
        
    headers = []
    headers.append('sim #')
    for par in range(len(params)):
        headers.append(params[par])    
    
    headers.append('cluster eu')
    headers.append('cluster sp')

    df = pd.DataFrame(pp,columns=headers)
    df = df.sort_values(by=['cluster eu','cluster sp'])    
    return df
    
'''
### Prepare data ###     

#files = ['fig7_theta0ClosedNoUser','fig7_theta0ClosedUser','fig7_theta0OpenNoUser','fig7_theta0OpenUser','fig7_theta1ClosedNoUser','fig7_theta1ClosedUser','fig7_theta1OpenNoUser','fig7_theta1OpenUser']
files = ['fig7_theta0OpenUser']


sims = 5000
params = ['c','a','F0','alpha','gamma','ra','tau','gamma\'']
var_name = 'Combined adopter fraction[eu]'
var_name2 = 'Combined adopter fraction[sp]'


sel1=dict() 
sel2=dict()
data = dict()

#data1=pd.read_csv(files[0]+'.tab',sep='\t')
#start=np.where(data1['Time']==4)[0][0] 
#data[files[i]]['Time']==4]

for i in range(len(files)):
    data[files[i]] = pd.read_csv(files[i]+'.tab',sep='\t')
    start=np.where(data[files[i]]['Time']==4)[0][0]    
    sel1[files[i]] = select(data[files[i]],params,'collapse')
    sel2[files[i]] = select(data[files[i]],params,'growth')

    #writer = pd.ExcelWriter(files[i]+'_'+dt+'.xlsx') #, engine='xlsxwriter')
    #sel1[files[i]].to_excel(writer, sheet_name='collapse')
    #sel2[files[i]].to_excel(writer, sheet_name='growth')
    #writer.save()





# Select data
d = data['fig7_theta0OpenUser'] #OpenUser

xx = []
ss = []
y = []
for i in range(1,sims+1):
    col = 'S'+str(i)+' '+var_name
    xx.append(d[col])
    ss.append(luok(d[col]))

u= list(set(ss))

'''

### FIGURE 7 ###

fig, ax = plt.subplots()
#plt.clf()

t = d['Time']
legendi1 = True
legendi2 = True
#legendi3=True
cl1_indexes = []
cl2_indexes = []
for i in range(len(xx)):
    if ss[i] !='+' and ss[i] != '-':                
        al = 1
        lw=2
        if ss[i] == '+0-' or ss[i] == '+-':  # cluster 2
            c = 'r--'
            al = 1
            lw = 1
            cl2_indexes.append(i)
        elif ss[i] == '-0+' or ss[i]=='-+':  
            c = 'k--'
            al = 0
            lw = 0.5
        elif ss[i] == '+0-0+' or ss[i]=='+-0+' or ss[i]=='+0-+':   # cluster 1
            c = 'k-'
            al = 1
            lw=1
            cl1_indexes.append(i)
        else:
            al = 0
            c = 'bo-'
            lw = 0.2
            print(ss[i])

        #if c == 'k--' and legendi1:
        #    plt.plot(t,xx[i],c,linewidth=lw,alpha=al,label='Cluster 1: Decline-growth')
        #    legendi1=False
                
        if c=='k-' and legendi1:
            plt.plot(t,xx[i],c,linewidth=lw,alpha=al,label='Cluster 1: Growth-decline-growth')
            legendi1=False
        elif c=='r--' and legendi2 and not legendi1:
            plt.plot(t,xx[i],c,linewidth=lw,alpha=al,label='Cluster 2: Growth-decline')
            legendi2=False
        else:
            plt.plot(t,xx[i],c,linewidth=lw,alpha=al,label='')


plt.ylim([0.0,0.05])
#plt.legend(loc=0,framealpha=0.5)
plt.suptitle('Adopter fraction', **hfont,fontsize=titlesize)
plt.title('(end users, both platforms)', **hfont,fontsize=titlesize_small)
plt.xlabel('Time', **hfont,fontsize=xlabelsize)

ax.set_xticks([0,20])                                                       
#ax.set_xticks([0,10,20,30], minor=True)                                           
ax.set_yticks([0.0,0.05])                                                       
#ax.set_yticks([0,0.2,0.4,0.6,0.8,1], minor=True) 
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False) 
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

box = ax.get_position()
ax.set_position([box.x0, box.y0+ box.height * 0.2, box.width, box.height*0.8])
ax.legend(loc='upper center', bbox_to_anchor=(0.5,-0.15), ncol=1,framealpha=0,fontsize=legendsize)
        

fig = plt.gcf()
fig.set_size_inches(w_single,h_single)
plt.savefig('fig7'+dt+'.jpg',dpi=mydpi) 



'''
fig, ax = plt.subplots()

for i in cl1_indexes:
    if i==cl1_indexes[0]:
        labeli='Cluster 1: Growth-decline-growth'
    else:
        labeli=''
    plt.plot(t,xx[i],'k-',linewidth=1,alpha=1,label=labeli)


#plt.plot(t,xx[108],'k-',linewidth=1,alpha=1,label='')
#plt.plot(t,xx[2649],'k-',linewidth=1,alpha=1,label='')
#plt.plot(t,xx[3495],'k-',linewidth=1,alpha=1,label='')
#plt.plot(t,xx[3679],'k-',linewidth=1,alpha=1,label='')
#plt.plot(t,xx[3787],'k-',linewidth=1,alpha=1,label='')
#plt.plot(t,xx[4586],'k-',linewidth=1,alpha=1,label='')


for i in cl2_indexes:
    if i==cl2_indexes[0]:
        labeli='Cluster 2: Growth-decline'
    else:
        labeli=''
    plt.plot(t,xx[i],'r--',linewidth=1,alpha=1,label=labeli)


#[834, 1670, 2595, 3208, 3265, 3851, 4529]
#plt.plot(t,xx[834],'r--',linewidth=1,alpha=1,label='')
#plt.plot(t,xx[1670],'r--',linewidth=1,alpha=1,label='')
#plt.plot(t,xx[2595],'r--',linewidth=1,alpha=1,label='')
#plt.plot(t,xx[3208],'r--',linewidth=1,alpha=1,label='')
#plt.plot(t,xx[3265],'r--',linewidth=1,alpha=1,label='')
#plt.plot(t,xx[3851],'r--',linewidth=1,alpha=1,label='')
#plt.plot(t,xx[4529],'r--',linewidth=1,alpha=1,label='')


plt.ylim([0,0.05])
#plt.legend(loc=0,framealpha=0.5)
plt.suptitle('Adopter fraction', **hfont,fontsize=titlesize)
plt.title('(end users, both platforms)', **hfont,fontsize=titlesize_small)
plt.xlabel('Time', **hfont,fontsize=xlabelsize)

ax.set_xticks([0,20])                                                       
#ax.set_xticks([0,10,20,30], minor=True)                                           
ax.set_yticks([0,0.05])                                                       
#ax.set_yticks([0,0.2,0.4,0.6,0.8,1], minor=True) 
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False) 
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

box = ax.get_position()
ax.set_position([box.x0, box.y0+ box.height * 0.2, box.width, box.height*0.8])
ax.legend(loc='upper center', bbox_to_anchor=(0.5,-0.15), ncol=1,framealpha=0,fontsize=legendsize)
        
fig = plt.gcf()
fig.set_size_inches(w_single,h_single)
plt.savefig('fig7a'+dt+'.jpg',dpi=mydpi) 
'''