# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 13:35:07 2014

@author: jgiesler
"""
import itertools
def is_prime(n):
    '''checks if n is prime'''    
    n= abs(int(n))
    
    if n<2:
        return False
    if n==2:
        return True
    if not n & 1:
        return False
        
    for x in range(3,int(n**.5)+1,2):
        if n%x==0:           
            return False
            
    return True
    
def is_pandigital(x):
    length = len(str(x))
    set_sol = set()
    for i in str(x):
        if i in set_sol:
            return False
        else:
            set_sol.add(i)
    for i in range(1,length+1):
        if str(i) not in set_sol:
            return False
    return True   
    
    
x = 9
while(x>0):
    combs = list(itertools.permutations('123456789',x))
    solu = list()
    for i in combs:
        solu.append(''.joinin(j for j in i))
    solu = list(map(int,solu))
    
    i = len(solu)-1
    while(i>=0):
        if(is_prime(solu[i]) and is_pandigital(solu[i])):
            print(solu[i])
            i = -1
        else:
            i -= 1
    x -= 1