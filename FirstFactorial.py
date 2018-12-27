#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:42:14 2018

@author: howardhsu
"""
def FirstFactorial(num): 
    
    a = int(1)
    num = int(num)
    
    for i in range(1, num+1):
        a = a * i

    # code goes here 
    return (a)
    
# keep this function call here  
print(FirstFactorial(input()))
