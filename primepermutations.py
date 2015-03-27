# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 12:46:21 2014

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
    

def are_permutations_prime(n):
    combs = list(itertools.permutations(str(n),4))
    print(combs)
    solu = list()
    for i in combs:
        if len(i)==4:
            solu.append(''.join(j for j in i))
    solu = list(set((map(int,solu))))
    count = 0
    for i in solu:
        if is_prime(int(i)):
            count += 1
    print(solu)
    if count > 3:
        solu.sort(reverse = True)
        if solu[0]-solu[1] == solu[1]-solu[2]==solu[2]-solu[3]:   
            print(solu)
            return True

    return False

for i in range (1000,9999):
    if are_permutations_prime(i):
        print(i)

        


