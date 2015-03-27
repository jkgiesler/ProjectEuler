'''
find all numbers 1-1,000,000 which 
are palandromes in base 10 and base 2
'''



def is_palindrome(x):
	'''will take a number and make it a string'''
	x=str(x)
	x_backwards=x[::-1]
	if x == x_backwards:
		return True
	else:
		return False

def to_binary_fixed(x):
	'''has to be a number'''
	binary_x = bin(x)[2:]
	return binary_x

nums=[]
for i in range(1000000):
	if is_palindrome(i) and is_palindrome(to_binary_fixed(i)):
		nums.append(i)

print(sum(nums))