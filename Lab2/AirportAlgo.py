# -*- coding: utf-8 -*-
"""CMPE 365 - Lab 1 (not for grades) Implement dijkstras algorithm"""
import numpy as np
#read in text file
with open("2019_Lab_2_flights_test_data.txt") as textFile:
    lines = [line.split() for line in textFile]

arraySize = int(lines[0][0])
print(arraySize)

#construct 2d Array


import numpy as np
import array
import pandas as pd
import math
INFINITY = float("inf")

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

A = 0
target = 3
cost = [A]*arraySize
predecessor = [A]*arraySize
reached = [False]*arraySize
reached[A] = True
estimate = [99999]*arraySize
candidate = [False]*arraySize
x = {}
prev = {
            "source": -1,
            "dest": -1,
            "depart":-1,
            "arrive":-1
        }

for i in schedule_df.index:
    x = {
            "source": schedule_df['source'][i],
            "dest": schedule_df['dest'][i],
            "depart":schedule_df['depart'][i],
            "arrive":schedule_df['arrive'][i]
            }
    if(x["source"] == prev["source"]):
        if(x["arrive"] < prev["arrive"]):
            estimate[x["dest"]] = x["arrive"]
            candidate[x["dest"]] = True
    elif(candidate[x["source"]] and (x["arrive"] < estimate[x["dest"]])):
        estimate[x["dest"]] = x["arrive"]
        candidate[x["dest"]] = True
        candidate[prev["dest"]] = False
        reached[prev["dest"]] = True
        predecessor[x["source"]] = prev["source"]
    prev = x
        
best_candidate = 99999
num_reach = reached.count(True)
#while num_reach != arraySize:
    
            
    
        
        
    
        

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



                
        
