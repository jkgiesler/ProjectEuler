# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 19:12:44 2014

@author: jgiesler
"""
from multiprocessing import Pool

def ranger(x):
    num = x 
    lst=[]
    while(num != 1):
        if num % 2 ==0:
            num = num/2
        else:
            num = 3*num + 1
        lst.append(num)
    size=len(lst)
    return [size,x]

if __name__ == '__main__':
    pool=Pool(processes=4)
    results = pool.map(ranger,list(range(1,1000000)))
    results.sort(reverse=True)
    print(results[0][1])

    