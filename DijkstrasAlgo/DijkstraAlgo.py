# -*- coding: utf-8 -*-
"""CMPE 365 - Lab 1 (not for grades) Impletment dijkstras algorithm"""

with open("Dijkstra_Data_6.txt") as textFile:
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
d = [0]*arraySize
vertex = 0
for i in range(arraySize):
    counter = 0
    for j in new_arr:
        d[counter] = j[vertex]
        counter = counter + 1
    print("Vertex {} furthest from vertex {} - Cost: {}\n".format(str(vertex), str(d.index(max(d))), str(max(d))))
    vertex = vertex + 1
        
