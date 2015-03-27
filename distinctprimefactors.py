# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 13:19:55 2014

@author: jgiesler
"""
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return set(factors)

canidate = list()
for i in range(1000,1000000):
    if len(prime_factors(i)) == 4:
        canidate.append(i)
        
for i in range(len(canidate)):
    if i > 4:
        if(canidate[i]-canidate[i-1] == 1 and \
        canidate[i-1]-canidate[i-2] == 1 and \
        canidate[i-2]-canidate[i-3] == 1):
            
            print(canidate[i-3])
        


        

