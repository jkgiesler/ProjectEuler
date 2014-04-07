'''
what is the sum of all amicable numbers
below 10000?
'''


def returndivisors(n):
    '''returns all divisors of number n'''    
    divisors=[] 
    for x in range(1,n+1): #slow method
        if n%x==0 and n != x:
            divisors.append(x)
    return divisors

amicable=[]
for i in range(10001):
    testcase=sum(returndivisors(i))
    
    if ((sum(returndivisors(testcase))==i) and (i != testcase)):
        amicable.append(i)

print(sum(amicable))
