# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 12:09:52 2014

@author: jgiesler
"""
import itertools

def is_special(string):
    return (int(string[1:4]) % 2 == 0)  and \
           (int(string[2:5]) % 3 == 0)  and \
           (int(string[3:6]) % 5 == 0)  and \
           (int(string[4:7]) % 7 == 0)  and \
           (int(string[5:8]) % 11 == 0) and \
           (int(string[6:9]) % 13 == 0) and \
           (int(string[7:]) % 17 == 0)
           



print(is_special('1406357289'))


combs = list(itertools.permutations('0123456789',10))
sum_num =0
solu = list()
for i in combs:
    if is_special(''.join(j for j in i)):
        sum_num += int(''.join(j for j in i))
        
print(sum_num)



#solu = list(map(int,solu))