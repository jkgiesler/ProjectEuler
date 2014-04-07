'''
calculate the first 1000 digit fibonocci number's position
in the sequence
'''


###Problem 2###
def fibgenerator():
    '''
    calculate all fibonocci numbers
    '''
    num=1
    oldnum=0
    nextnum=0
    sumer=0
    while(True):
        nextnum=oldnum+num
        oldnum=num
        num=nextnum
        yield num
        

x=fibgenerator()
n=1
count=1
bignum= int('1'+'0'*999) #make a number 1000 ints long
while(n<bignum):
    n=next(x)
    print(n)
    count+=1

print(count)
