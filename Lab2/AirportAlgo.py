# -*- coding: utf-8 -*-
"""CMPE 365 - Lab 2: Airport flights"""
import numpy as np
import array
import pandas as pd
import math
from itertools import *
#read in text file to get number of points
with open("2019_Lab_2_flights_test_data.txt") as textFile:
    lines = [line.split() for line in textFile]

arraySize = int(lines[0][0])
print(arraySize)

INFINITY = float("inf")

#construct 3d array from text file
with open('2019_Lab_2_flights_test_data.txt') as file:
    file_contents = file.read()
    #print(file_contents)


file = np.array(file_contents.split())

vCount = int(file[0],10)

file_contents = file_contents[1:]
cost = np.zeros(vCount)

reached = np.zeros(file.size - 1, dtype=bool)
reached[0] = True
rows, cols = map(int, [14,4])

data = map(int, file_contents.split())

mat = [*map(list, zip(*[data] * cols))]

i = 0;

schedule = []
 
for i in range(vCount):
     l = []
     for d in mat:
         if d[0] == i:
             l.append(d)
     schedule.append(l)
#print(schedule)

start = 0;
end = 3;

Cost = [0]*vCount
estimate = [INFINITY]*vCount
Candidate = [False]*vCount
Cost[start] = 0;
Predecessor = Cost[:]
Reached = Candidate[:]

Cost[start] = 0
Reached[start] = True

#read data into pandas dataframe
schedule = list(chain(*schedule))
schedule_df = pd.DataFrame(columns=["source", "dest", "depart", "arrive"])
s = []
d1 = []
d2 = []
a = []
for i in schedule:
    s.append(i[0])
    d1.append(i[1])
    d2.append(i[2])
    a.append(i[3])
schedule_df["source"] = s
schedule_df["dest"] = d1
schedule_df["depart"] = d2
schedule_df["arrive"] = a

#function to calculate shortest flight route (main objective of lab)
def flightPath(start, target, s_df):
    #initialize variables
    A = start
    target = target
    schedule_df = s_df
    cost = [None]*arraySize
    cost[A] = 0
    predecessor = [None]*arraySize
    reached = [False]*arraySize
    reached[A] = True
    estimate = [99999]*arraySize
    candidate = [False]*arraySize
    x = {}
    prev_vert = -1
    direct_cost = 99999
    prev = {
                "source": -1,
                "dest": -1,
                "depart":-1,
                "arrive":-1
            }
    #filter dataframe to only get flight routes of starting point
    source_df = schedule_df[schedule_df["source"] == A]
    for i in source_df.index:#iterate over filtered dataframe to get eligible candidate
        x = {
                "source": source_df['source'][i],
                "dest": source_df['dest'][i],
                "depart":source_df['depart'][i],
                "arrive":source_df['arrive'][i]
                }
        if(x["dest"] == target and x["arrive"] < direct_cost):
            direct_cost = x["arrive"] #save arrival time of direct flight (if exists)
        if(x["arrive"] < prev["arrive"] or prev["arrive"] == -1):
            estimate[x["dest"]] = x["arrive"]
            candidate[prev["dest"]] = False
            candidate[x["dest"]] = True
        prev = x # keep track of previous flight route
    predecessor[A] = -1
    prev_vert = A
    #continue to loop until target is not reached
    while (not reached[target]):
        best_candidate = 99999
        v = 1
        for i in range(arraySize):#find best candidate
            if(candidate[i] and estimate[i] < best_candidate):
                v = i
                best_candidate = estimate[i]
        if(best_candidate == 99999):
            print("City is unreachable")
            break
        #update values of candidate
        cost[v] = estimate[v]
        reached[v] = True
        candidate[v] = False
        v_df = schedule_df[schedule_df["source"] == v] #filter for flight routes of candidate
        #update potential candidates
        for z in v_df.index:
            if((v_df["depart"][z] > estimate[v]) and (not reached[v_df["dest"][z]])):
                candidate[v_df["dest"][z]] = True
            if((v_df["arrive"][z] < estimate[v_df["dest"][z]]) and (candidate[v_df["dest"][z]])):
                estimate[v_df["dest"][z]] = v_df["arrive"][z]
                predecessor[v] = prev_vert
        if(v != target):
            prev_vert = v
    predecessor[target] = prev_vert
    #if direct flight arrives earlier use direct route
    if(direct_cost <= cost[target]):
        cost = [None]*arraySize
        cost[A] = 0
        cost[target] = direct_cost
        predecessor = [None]*arraySize
        predecessor[A] = -1
        predecessor[target] = A
        reached = [False]*arraySize
        reached[A] = True
        reached[target] = True
    #print statements
    print(cost)
    print(predecessor)
    print(reached)
    print("The fastest way to get from {} to {} has an arrival time of {}".format(A, target, cost[target]))
    
flightPath(0, 3, schedule_df)#function call
    


    
    
        
    
            
        
    
    
            
    
        
        
    
        

#num_points = int(lines[0].pop(0))
#lines.pop(0) 
#algorithm
"""def dijkstra(arr):
    #initialize arrays
    A = 0
    W = arr
    cost = [A]*arraySize
    predecessor = [A]*arraySize
    reached = [False]*arraySize
    reached[A] = True
    estimate = [99999]*arraySize
    candidate = [False]*arraySize
    for k in range(arraySize):
        if(W[A][k] > 0):
            estimate[k] = W[A][k]
            candidate[k] = True
    predecessor[A] = -1
    num_reach = 1
    most_distant = A
    while(arraySize != num_reach):
        best_candidate = 99999
        v = 1
        for x in range(arraySize):
            if(candidate[x] and estimate[x] < best_candidate):
                v = x
                best_candidate = estimate[x]
        if(best_candidate == 99999):
            break
        cost[v] = estimate[v]
        reached[v] = True
        candidate[v] = False
        if(cost[v] > cost[most_distant]):
            most_distant = v
        for z in range(arraySize):
            if(W[v][z] > 0 and reached[z] == False):
                candidate[z] = True
                if(cost[v] + W[v][z] < estimate[z]):
                    estimate[z] = cost[v] + W[v][z]
                    predecessor[z] = v
        num_reach = num_reach + 1
    if(arraySize != num_reach):
        print("Not all points were reachable")
    print("The vertex furthest from vertex {} is vertex {}, which has a cost of {}".format(str(A), str(most_distant), str(cost[most_distant])))"""



                
        
