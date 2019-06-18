#!/usr/bin/python
# -*- coding: UTF-8 -*-

for i in range(2,1000):
    sum=0
    for j in range(1,i):
        if i%j==0:
            # print(j,end=' ')
            sum+=j
    if sum==i:
        print(i)