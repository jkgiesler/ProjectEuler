from math import *
'''
find a b c for a^2+b^2=c^2 and a+b+c=1000
'''
solu = dict()
for x in range(1000):
	solu[x] = 0
	for a in range(x):
	    for b in range(x-a):
	        if sqrt(a**2+b**2)+a+b==x:
	            c=(x-(a+b))
	            if (a**2+b**2==c**2):
	           		solu[x] += 1

	print solu[x]

largest = 0
largestkey = 0

for i in list(solu.keys()):


	if(solu[i] > largest):
		largest = solu[i]
		largestkey = i

print(largestkey)