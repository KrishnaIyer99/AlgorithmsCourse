# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 19:36:19 2019

@author: krish
"""

from collections import Counter
from heapq import heappush, heappop, heapify

def code_building():
    #get character frequency from text file
    with open("EarthASCII.txt") as f:
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
    file = open("CodeBuilder.txt", "w+")
    file.write("ASCII -> CODE\n")
    for symbol, code in codes_dict.items():
        file.write("%d -> %s" % (ord(symbol), code) +"\n")
    file.close()
    return codes_dict

def encoder(converter):
    file_name = input("Enter file name: ")
    f = open(file_name)
    content = f.read()
    f_encoded = open("EncodedFile.txt", "w+")
    for c in content:
        f_encoded.write(converter[c])
    f_encoded.close()
    f.close()

def decoder(converter):
    file_name = input("Enter name of encoded file name: ")
    f = open(file_name)
    digits = list(f.read())
    f.close()
    f_decoded = open("decoderFile.txt", "w+")
    start = 0
    end = 0
    window = []
    decoder = dict([(v,k) for k, v in converter.items()])

    while end<len(digits):
        myString = ""
        myString = myString.join(window)
        if start == end:
            window = [digits[start], digits[end+1]]
            end+= 1

        if myString in decoder.keys():
            f_decoded.write(decoder[myString])
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
    
    
    
    
    
    
    





    
"""
    
    
    



    


frequencyTree = {}
frequencyTree[chr(10)] = 0
for l in range(32, 127):
   frequencyTree[chr(l)] = 0
with open("EarthASCII.txt") as f:
    content = f.read()

for char in content:
    frequencyTree[char] += 1

heap = [[wt, [sym, ""]] for sym, wt in frequencyTree.items()]

heapify(heap)
while len(heap) > 1:
    lo = heappop(heap)
    hi = heappop(heap)
    for pair in lo[1:]:
        pair[1] = '0' + pair[1]
        #print("lo")
        #print(pair)
    for pair in hi[1:]:
        pair[1] = '1' + pair[1]
        #print(hi)
        #print(pair)
    heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    #print(heap)
huff = sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

    
"""     