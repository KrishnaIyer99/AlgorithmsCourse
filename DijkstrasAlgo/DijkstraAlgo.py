# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

with open("C:\\Users\\Krishna Iyer\\Desktop\\Dijkstra_Data_6.txt") as textFile:
    lines = [line.split() for line in textFile]

arraySize = int(lines[0][0])
print(arraySize)
