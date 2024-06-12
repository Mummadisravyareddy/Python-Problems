# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 09:11:08 2024

@author: mtanu
"""
"""program to present the list of values to the given format"""
s=[4,0,5,0,1,9,0,0]
j=0
for i in range(0,8):
        if(s[i]!=0):
            s[j]=s[i]
            j=j+1
while j<8:
    s[j]=0
    j=j+1
print(s)
