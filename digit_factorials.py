'''
find all numbers which equal to their digits factorial
1!4!5! = 145
'''


import math

def check_it(num):
	sum=0
	str_i=str(num)
	for i in str_i:
		z=int(i)
		sum+=math.factorial(z)
	if sum == num:
		return True
	else:
		return False

success=[]		
for i in range(1000000):
	if check_it(i):
		success.append(i)
print(success)