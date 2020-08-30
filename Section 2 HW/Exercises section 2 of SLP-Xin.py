# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 21:00:30 2020

@author: Cinker
"""

# 2.6 Now implement a minimum edit distance algorithm and use your 
# hand-computed results to check your code.

import numpy as np # matrix operation

def meDis(str1, str2):
    # del-cost
    del_cost = 1
    # ins-cost
    ins_cost = 1
    # sub-cost
    sub_cost = 2
    
    m = len(str1)
    n = len(str2)
    
    # initialization of the distance matrix
    k = max(m,n)
    D = np.zeros((k+1,k+1))
    D[0,:] = range(0,k+1)
    D[:,0] = range(0,k+1)
    
    if k == m: # str1 longer
        str2 = str2 + " "*(m-n)
    else:
        str1 = str1 + " "*(n-m)
    
    for i in range(1,k+1):
        for j in range(1,k+1):
            if str1[i-1] == str2[j-1]:
                sub_cost = 0
            else:
                sub_cost = 2
            D[i,j] = min(D[i-1,j] + del_cost, D[i,j-1] + ins_cost, D[i-1,j-1] + sub_cost)
    
    print(D)


meDis("drive", "brief")
meDis("drive", "drivers")

def meDisbacktrace(str1, str2):
    # del-cost
    del_cost = 1
    # ins-cost
    ins_cost = 1
    # sub-cost
    sub_cost = 2
    
    m = len(str1)
    n = len(str2)
    
    # initialization of the distance matrix
    k = max(m,n)
    D = np.zeros((k+1,k+1))
    D[0,:] = range(0,k+1)
    D[:,0] = range(0,k+1)
    
    d_trace = D.astype(np.str)
    
    if k == m: # str1 longer
        str2 = str2 + " "*(m-n)
    else:
        str1 = str1 + " "*(n-m)
    
    for i in range(1,k+1):
        for j in range(1,k+1):
            if str1[i-1] == str2[j-1]:
                sub_cost = 0
            else:
                sub_cost = 2
            D[i,j] = min(D[i-1,j] + del_cost, D[i,j-1] + ins_cost, D[i-1,j-1] + sub_cost)
            d_trace[i,j] = np.str(D[i,j])
            if D[i,j] == D[i-1,j] + del_cost:
                d_trace[i,j] = "↑"+d_trace[i,j]
            if D[i,j] == D[i,j-1] + ins_cost:
                d_trace[i,j] = "←"+d_trace[i,j]
            if D[i,j] == D[i-1,j-1] + sub_cost:
                d_trace[i,j] = "↖"+d_trace[i,j]
    print(d_trace)
    
meDisbacktrace("drive", "drivers")















