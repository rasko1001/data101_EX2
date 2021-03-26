# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 15:32:07 2021

@author: Noam
"""


def revword(str):
    t = str.lower()
    word = ""
    
    for char in t:
        word = char + word 
    return word


def countword():
    #path = r'text.txt'
    f = open('text.txt', "r").read()
    #with open('filename') as f:
    #    lines = f.readlines()
    f = f.splitlines()
    word = f[0]
    count  = 1
    print(word)
    
    for line in f:
        tline = line.split(sep = " ")
        for tword in tline:
            if word == revword(tword):
                count = count + 1

    return count

#print(revword("dlroW"))   
#print(countword()) 


    
    