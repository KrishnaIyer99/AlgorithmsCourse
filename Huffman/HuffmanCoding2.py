# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 17:05:44 2019

@author: Krishna Iyer
"""
from collections import Counter
from heapq import heappush, heappop, heapify
import os

def code_building(input_f, output_f):
    #get character frequency from text file
    with open(input_f) as f:
        c = Counter(f.read().strip())
        f = c.most_common()#order characters from high freq to low
    
    ftree = {}
    ftree[chr(10)] = 0
    for z in range(32, 127):
        ftree[chr(z)] = 0
    for y in f:
        ftree[y[0]] += y[1]
    freq_lst = [[v,[k,""]] for k, v in ftree.items()]
    heapify(freq_lst)
    
    while(len(freq_lst)>1):
        low_br = heappop(freq_lst)
        high_br = heappop(freq_lst)
        for l in low_br[1:]:
            l[1] = "0{}".format(str(l[1]))
        for h in high_br[1:]:
            h[1] = "1{}".format(str(h[1]))
        #hi[2] = "1"+hi[2]
        heappush(freq_lst, [low_br[0]+high_br[0]]+low_br[1:]+high_br[1:])#merge nodes and push to heap
    codes_dict = dict(sorted(heappop(freq_lst)[1:], key=lambda k: (len(k[-1]), k)))
    file = open(output_f, "w+")
    file.write("ASCII -> CODE\n")
    for symbol, code in codes_dict.items():
        file.write("%d -> %s" % (ord(symbol), code) +"\n")
    file.close()
    return codes_dict

def encoder(converter, output_f):
    file_name = input("Enter file name: ")
    f = open(file_name)
    content = f.read()
    f_encoded = open(output_f, "w+")
    for c in content:
        f_encoded.write(converter[c])
    f_encoded.close()
    f.close()

def decoder(converter, decoded_f):
    file_name = input("Enter name of encoded file name: ")
    f = open(file_name)
    digits = list(f.read())
    f.close()
    f_decoded = open(decoded_f, "w+")
    start = 0
    end = 0
    window = []
    decoder = dict([(v,k) for k, v in converter.items()])

    while end<len(digits):
        bits = ""
        bits = bits.join(window)
        if start == end:
            window = [digits[start], digits[end+1]]
            end+= 1

        if bits in decoder.keys():
            f_decoded.write(decoder[bits])
            #print(myString)
            #print(decoder[myString]+"\n")
            end+=1
            start = end
            if(end+1) < len(digits):
                window = [digits[start], digits[end+1]]
        else:
            end+=1
            window.extend(digits[end])
    f_decoded.close()


#Combine all data files to be converted
with open("DATA.txt", 'w') as outfile:
    for f in os.listdir("Data 20191031"):
        file = open("Data 20191031"+'/'+f)
        content = file.read()
        outfile.write(content)
        file.close()
    outfile.close()


#Canonical Collection 1

codes = code_building("Canonical Collection 1 20191031\\"+os.listdir("Canonical Collection 1 20191031")[0], "CC1Codes.txt")
encoder(codes, "DATA-CC1.txt")

#Canonical Collection 2

#Combine all files to get total frequency
with open("CC2.txt", 'w') as outfile:
    for f in os.listdir("Canonical Collection 2 20191031"):
        file = open("Canonical Collection 2 20191031"+'/'+f)
        content = file.read()
        outfile.write(content)
        file.close()
    outfile.close()

codes = code_building("CC2.txt", "CC2Codes.txt")
encoder(codes, "DATA-CC2.txt")

#Canonical Collection 3
#Combine all files to get total frequency
with open("CC3.txt", 'w') as outfile:
    for f in os.listdir("Canonical Collection 3 20191031"):
        file = open("Canonical Collection 3 20191031"+'/'+f)
        content = file.read()
        outfile.write(content)
        file.close()
    outfile.close()

codes = code_building("CC3.txt", "CC3Codes.txt")
encoder(codes, "DATA-CC3.txt")




















