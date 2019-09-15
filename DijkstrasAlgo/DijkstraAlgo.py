# -*- coding: utf-8 -*-
"""CMPE 365 - Lab 1 (not for grades) Impletment dijkstras algorithm"""

with open("C:\\Users\\Krishna Iyer\\Desktop\\Dijkstra_Data_6.txt") as textFile:
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
print(new_arr)
