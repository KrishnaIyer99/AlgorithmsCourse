# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:37:16 2019

@author: krish"""
import numpy as np
import random
import copy




def BFI_subset_sum(S,k):
    subsets = []
    empty_set = {
            "set": [],
            "sum": 0
            }
    subsets.append(empty_set)
    
    for i in S:
        new_subsets = []
        for old in subsets:
            new_set = {
                    "set": copy.copy(old["set"]),
                    "sum":0
                    }
            new_set["set"].append(i)
            new_set["sum"] = sum(new_set["set"])
            new_subsets.append(new_set)
            if new_set["sum"] == k:
                return new_set
        subsets = copy.deepcopy(new_subsets)
        print(subsets)
    return "No subsets found"


Set = [3,5,3,9,18,4,5,6]

output = BFI_subset_sum(Set, 9)
print(output)
    
            
            
        
    
    