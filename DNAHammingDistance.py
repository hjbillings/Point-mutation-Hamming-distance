#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 23:39:17 2020

@author: hanabillings
"""

"""
Given: Two DNA strings s and t of equal length, return the Hamming distance dH(s,t).
"""

def getHamming(sequences):
    ham = 0
    seq1 = sequences[0]
    seq2 = sequences[1]
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            ham += 1
        elif seq1[i] == seq2[i]:
            i = i+1
    return ham
    
    

sequences = "GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT" 
print(getHamming(sequences))
