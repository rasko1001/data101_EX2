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
    path = r'C:\Users\Noam\Desktop\studies\data101\EX2\text.txt'
    f = open(path, "r").read()
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

print(revword("dlroW"))   
print(countword()) 


    
    