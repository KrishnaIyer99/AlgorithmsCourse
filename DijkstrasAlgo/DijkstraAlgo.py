# -*- coding: utf-8 -*-
"""CMPE 365 - Lab 1 (not for grades) Implement dijkstras algorithm"""
#read in text file
with open("Dijkstra_Data_1600.txt") as textFile:
    lines = [line.split() for line in textFile]

arraySize = int(lines[0][0])
print(arraySize)

#construct 2d Array
new_arr = []
for i in range(arraySize+1):
    if(lines[i] == lines[0]):
        continue
    else:
        row = []
        for j in range(arraySize):
            row.append(int(lines[i][j]))
        new_arr.append(row)

#algorithm
def dijkstra(arr):
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
    print("The vertex furthest from vertex {} is vertex {}, which has a cost of {}".format(str(A), str(most_distant), str(cost[most_distant])))
                
        
