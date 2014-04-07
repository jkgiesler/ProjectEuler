'''
look for unique powers

a**b

2--100 a
2--100 b

'''
lst=[]
for a in range (2,101):
    for b in range(2,101):
        print(a)
        lst.append(a**b)
z=set(lst)
print(len(list(z)))

'''
fifth powers
Find the sum of all the numbers 
that can be written as the sum 
of fifth powers of their digits.
'''

cond=True
strt=2
sumr=0
while(cond):
    short_sum=0
    for i in list(str(strt)):
        short_sum+=int(i)**5
    if str(short_sum)==str(strt):
        sumr+=int(strt)
    strt+=1
    print(sumr)