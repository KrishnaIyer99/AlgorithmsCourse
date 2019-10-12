# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:37:16 2019

@author: krish"""

import pandas as pd
import random
import math
from statistics import mean
def create_obj(array): #helper function creates object from subset
    return {"set": array[:], "sum": sum(array)}

"""
PART 1: BRUTE FORCE ALGORITHM

def BFI_subset_sum(S,k):
    subsets = []
    subsets.append(create_obj([]))
    sums = []
    for i in S:
        new_subsets = []
        for old in subsets:
            #new_subsets.append(old)
            new_set = create_obj(old["set"]+[i])
            sums.append(new_set["sum"])
            if new_set["sum"] == k:
                return new_set
            else:
                new_subsets.append(old)
                new_subsets.append(new_set)
        subsets = new_subsets
        print(subsets)
        print(sums)
            
    return subsets
"""

"""
PART 2: HS ALGORITHM


def BFI_subset_sum(S,k):
    count = 0
    subsets = []
    subsets.append(create_obj([]))
    sums = []
    sets = []
    for i in S:
        new_subsets = []
        for old in subsets:
            #new_subsets.append(old)
            new_set = create_obj(old["set"]+[i])
            sums.append(new_set["sum"])
            sets.append(new_set["set"])
            new_subsets.append(old)
            new_subsets.append(new_set)
            if new_set["sum"] == k:
                return new_set
        subsets = new_subsets
    return (sums, sets)


def pair_sum(sum1, sum2, k):
    print(k)
    idx_1 = 0
    idx_2 = len(sum2)-1
    while(idx_1 <= len(sum1) and idx_2 >= 0):
        s = sum1[idx_1] + sum2[idx_2]
        #print(s)
        if s == k:
            return (sum1[idx_1], sum2[idx_2])
        elif s < k:
            idx_1 = idx_1 + 1
        else:
            idx_2 = idx_2 - 1
    return (-1, -1)
    
    

def HS_subset_sum(S, k):
    n = len(S)
    S_l = S[0:int(n/2)]
    S_r = S[int(n/2):n]
    left = BFI_subset_sum(S_l, k)
    right = BFI_subset_sum(S_r, k)
    
    if(type(left) == dict):
        return left
    elif(type(right) == dict):
        return right
    else:
        pd_right = pd.DataFrame(list(zip(right[0], right[1])), columns=["Sum", "Set"])
        #print(pd_right)
        pd_left = pd.DataFrame(list(zip(left[0], left[1])), columns=["Sum", "Set"])
        #print(pd_left)
        sum_right = right[0]
        sum_left = left[0]
        sum_right.sort()
        sum_left.sort()
        #print(left)
        sl, sr = pair_sum(sum_left, sum_right, k)
        print((sl, sr))
        if((sl, sr) != (-1, -1)):
            right_idx = pd_right.loc[pd_right["Sum"] == sr]
            left_idx = pd_left.loc[pd_left["Sum"] == sl]
            return(left_idx.iloc[0], right_idx.iloc[0])
        else:
            return "No subsets found"

Set = [3,5,3,9,18,4,5,6,61,7] #Test Set

output = HS_subset_sum(Set, 89)
if type(output) == tuple:
    output_set = output[0]["Set"] + output[1]["Set"]
    output_sum = output[0]["Sum"] + output[1]["Sum"]
    print(str(output_set) + ": " + str(output_sum))
else:
    print(output)
"""

#PART 3: TESTING - with comments for all functions

#Brute force implementation with operation counting
def BFI_subset_sum(S,k):
    count = 0
    subsets = []
    subsets.append(create_obj([])) # create empty set and add it to subsets list
    #initialize lists for sums and corresponding subset
    sums = []
    sets = []
    #iterate over all values of set S
    for i in S:
        new_subsets = []# keep track of all subsets in this iteration
        for old in subsets:
            new_set = create_obj(old["set"]+[i]) # create new set object by appending new value to previous subsets
            count = count + 2 #+1 for building subset and +1 for computing sum
            sums.append(new_set["sum"])
            sets.append(new_set["set"])
            new_subsets.append(old)# add previous subsets to new list
            new_subsets.append(new_set)
            if new_set["sum"] == k:
                return new_set, count
        subsets = new_subsets # overwrite new list to old list
        count = count + 1 # add to operations counter
    return (sums, sets), count # return sum and sets lists as tuple, return count as well


def pair_sum(sum1, sum2, k):
    #initialize operation counter and indexes
    count = 0
    idx_1 = 0
    idx_2 = len(sum2)-1
    while(idx_1 < len(sum1) and idx_2 >= 0): #loop with first index does not reach end and second does not reach beginning
        s = sum1[idx_1] + sum2[idx_2]
        count += 2
        #+2 for each value accessed from sum lists
        if s == k:
            count = count + 2
            return sum1[idx_1], sum2[idx_2], count
            #if target is reached return the sum values and cpunter
        elif s < k:
            idx_1 = idx_1 + 1 # increment first index by 1 if sum less than target
        else:
            idx_2 = idx_2 - 1 # decrement second index by 1 if sum less than target
    return -1, -1, count
    #return if target isnt reached
    

def HS_subset_sum(S, k):
    # intialize operation counter
    count = 0
    n = len(S) # get length of set
    #split set into two equally sized subsets
    S_l = S[0:int(n/2)]
    S_r = S[int(n/2):n]
    #use brute force on each inividual subset and add to the operation counter
    left = BFI_subset_sum(S_l, k)
    count += left[1]
    right = BFI_subset_sum(S_r, k)
    count += right[1]
    #check if target sum was found in either subset return
    if(type(left[0]) == dict):
        return left
    elif(type(right[0]) == dict):
        return right
    else:# if target sum was not found in either subset
        #read sums and corresponding subsets into pandas (one data frame for left and one for right)
        pd_right = pd.DataFrame(list(zip(right[0][0], right[0][1])), columns=["Sum", "Set"])
        count = count + 1
        pd_left = pd.DataFrame(list(zip(left[0][0], left[0][1])), columns=["Sum", "Set"])
        count = count + 1
        # sort list of sums
        sum_right = right[0][0]
        sum_left = left[0][0]
        sum_right.sort()
        sum_left.sort()
        #add to counter for sorting of each sum list
        count += int(2*(3*len(sum_right)*math.log(len(sum_right))))
        sl, sr, pair_count = pair_sum(sum_left, sum_right, k) # call pair sum to check for target between either subset
        count += pair_count
        if((sl, sr) != (-1, -1)):
            # return rows from dataframe with the correct sum value (also return counter)
            right_idx = pd_right.loc[pd_right["Sum"] == sr]
            left_idx = pd_left.loc[pd_left["Sum"] == sl]
            return(left_idx.iloc[0], right_idx.iloc[0]), count
        else:
            #if target is still not found
            return ("No subsets found"), count

#initialize arrays for each algo (stores a tuple with average operations and set size)
counts_HS = []
counts_BFI = []
#calculate average operations for each set size from 4 - 14
for n in range(4,15):
    #create arrays for store average values for each iteration
    avg_vals_BFI = []
    avg_vals_HS = []
    for i in range(1,20): # conduct 20 tests for each set size 
        #create random array set of n integer values from 0 - 100
        arr = [random.randint(1,100) for x in range(n)]
        targets = [random.randint(1,100) for z in range(10)] #randomly generate 10 target values
        counter1 = []
        counter2 = []
        for k in targets:
            # record operation counts for each k value in targets
            BFI = BFI_subset_sum(arr, k)
            HS = HS_subset_sum(arr, k)
            c1 = BFI[1]
            c2 = HS[1]
            counter1.append(c1)
            counter2.append(c2)
        #computer average operation count for the set
        avg1 = mean(counter1)
        avg2 = mean(counter2)
        avg_vals_BFI.append(avg1)
        avg_vals_HS.append(avg2)
    # create tuples that store average operations for n-sized set and the n value
    BFI_tuple = (mean(avg_vals_BFI), n)
    HS_tuple = (mean(avg_vals_HS), n)
    #append tuples to their corresponding algorithms arrays
    counts_HS.append(HS_tuple)
    counts_BFI.append(BFI_tuple)
    
#output results
print("HS Operations:")
print(counts_HS)
print("BFI Operations")
print(counts_BFI)

"""
Sample Output:

HS Operations:
[(42.61578947368421, 4), (113.15789473684211, 5), (123.22631578947369, 6), (288.13684210526316, 7), (283.3157894736842, 8), (685.2947368421053, 9), (651.8421052631579, 10), (1336.0526315789473, 11), (1371.6052631578948, 12), (3325.221052631579, 13), (2921.4, 14)]
BFI Operations
[(33.23684210526316, 4), (60.7, 5), (117.97368421052632, 6), (219.50526315789475, 7), (400.16315789473686, 8), (785.0, 9), (1341.1315789473683, 10), (2319.8736842105263, 11), (4531.88947368421, 12), (10751.494736842105, 13), (16478.22105263158, 14)]

"""



"""

Q/A - write up

Q: Do your observations support the theoretical predictions that BFI_Subset_Sum is in O(2^n) and HS_Subset_Sum is in O(n*2^n/2)?

A: Yes I do support the theoretical production because when you convert these functions from
   Big-O to regular functions BFI is y = 2^x and HS is y = x*2^(x/2). When analyzing the behaviour
   of these 2 functions it shows that 2^x is less than x*2^(x/2) for smaller values.
   However, once x becomes larger x*2^(x/2) becomes smaller than 2^x. This is seen in the 
   output of my experimentation results as the BFI function has fewer operations than the HS function
   until n = 7. With exceptions to a few results, it HS takes fewer operations than BFI as 
   the size of the set continues to grow.
"""


        

            
            

        
    
    
    

    
    