# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 19:36:19 2019

@author: krish
"""

from collections import Counter
from heapq import heappush, heappop, heapify
import pandas as pd
#get character frequency from text file
with open("EarthASCII.txt") as f:
    c = Counter(f.read().strip())
f = c.most_common()#order characters from high freq to low
i = len(f) - 1

ftree = {}
ftree[chr(10)] = 0
for z in range(32, 127):
    ftree[chr(z)] = 0
for y in f:
    ftree[y[0]] += y[1]
freq_lst = [(v,k,"") for k, v in ftree.items()]
heapify(freq_lst)

while(len(freq_lst)>1):
    lo = heappop(freq_lst)
    hi = heappop(freq_lst)
    lo[2] = "0"+lo[2]
    hi[2] = "1"+hi[2]
    
    
    
    



    

"""frequencyTree[chr(10)] = 0
for l in range(32, 127):
    frequencyTree[chr(l)] = 0
with open("EarthASCII.txt") as f:
    content = f.read()
for char in content:
    frequencyTree[char] += 1

heap = [[wt, [sym, ""]] for sym, wt in frequencyTree.items()]"""


        
