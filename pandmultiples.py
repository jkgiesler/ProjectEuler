'''
find the largest 9 digit pandigital number which can be made 
by concatinating an integer * n where n > 1
ie 192

192*1 = 192
192*2 = 384
192*3 = 576

192384576 is pandigital
'''

pandas = set()

def nottoobig(n):
	if n == -1:
		return False
	if len(str(n)) <= 9:
		if is_panda(n):
			return True
	else:
		return False

def is_panda(n):
	setr = set()
	setr.add("0")
	for i in str(n):
		if i in setr:
			return False
		else:
			setr.add(i)
	return True

def concat(n,old): 
	num = int(str(old)+str(n))
	if nottoobig(num):
		if len(str(num)) == 9 and n >1:
			print("it's a pandigital value: "+ str(num))
			pandas.add(num)
		return num
	else:
		return -1


for i in range(9488):
	num =''
	dig = 1
	old =''
	while nottoobig(old) and dig < 10:
		new = i * dig
		old = concat(new,old)
		dig+=1

print(max(list(pandas)))




