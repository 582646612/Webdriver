#!/usr/bin/python
# -*- coding: UTF-8 -*-

def jia(x,y):
    sum=0
    for i in range(1,x+1):
        z=0
        for j in range(1,i+1):
            a=10**(j-1)
            b=y*a
            z=z+b
        sum+=z
    print(sum)
jia(5,5)