# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 12:32:44 2014

@author: jgiesler
"""

##Problem 1###
def problem1():
    '''
    calculate the sum of all natural 
    numbers divisible by 3 or 5 from
    1 to 1000
    '''
    
    z=list(range(1,1000))
    
    num=[]
    for i in z:
        if((i%5==0) or (i%3==0)):
            #print(i)
            num.append(i)
            
    print(sum(num))
    
###Problem 2###
def problem2():
    '''
    calculate all fibonocci numbers below 4million
    and determine the sum of the even ones
    '''
    maxnum=4000000
    num=1
    oldnum=0
    nextnum=0
    sumer=0
    while(nextnum<maxnum):
        nextnum=oldnum+num
        oldnum=num
        num=nextnum
        if(oldnum%2==0):
            sumer+=oldnum
    
    print(sumer)
