# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 09:57:09 2024

@author: mtanu
"""

'''find factorial of no.'''
n=int(input("enter the number"))
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(n))