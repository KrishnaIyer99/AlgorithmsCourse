# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:37:16 2019

@author: krish"""

import pandas as pd


def create_obj(array):
    return {"set": array[:], "sum": sum(array)}

"""def BFI_subset_sum(S,k):
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
            
    return subsets"""
def BFI_subset_sum(S,k):
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
    S_r = S[int((n/2)):n]
    left = BFI_subset_sum(S_l, k)
    right = BFI_subset_sum(S_r, k)
    
    if(type(left) == dict):
        return left
    elif(type(right) == dict):
        return right
    else:
        pd_right = pd.DataFrame(list(zip(right[0], right[1])), columns=["Sum", "Set"])
        print(pd_right)
        pd_left = pd.DataFrame(list(zip(left[0], left[1])), columns=["Sum", "Set"])
        print(pd_left)
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
            return(left_idx, right_idx)
        else:
            return "No subsets found"

Set = [3,5,3,9,18,4,5,6]

output = HS_subset_sum(Set, 13)
print(output)
    
            
            
        
    
    