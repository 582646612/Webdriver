#!/usr/bin/python
# -*- coding: UTF-8 -*-

for n in range(100, 1000):
    i = int(n / 100)
    j = int(n / 10 % 10)
    k =int(n % 10)
    if n == i **3 + j *j*j + k *k*k:
        print(n)