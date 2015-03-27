# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 13:21:41 2014

@author: jgiesler
"""

triangle = set()
pentagon = set()
hexagon = set()


for i in range(1,1000000):
    triangle.add((i*(i+1))/2)
    pentagon.add((i*(3*i-1))/2)
    hexagon.add(i*(2*i-1))
    
solution = triangle & pentagon & hexagon

for i in solution:
    print(i)