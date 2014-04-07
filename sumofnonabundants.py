'''
find the sum of all numbers which cannot be made by
adding two abundant numbers together
'''

import math

def divisor_generator(n):
    '''
    returns all divisors including n and in some cases duplicates
    be careful
    '''
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors:
        yield int(divisor)

def is_abundant(n):
    '''returns an integer 0 def, 1 abundantnumber, 2 perfect number'''    
    divisors=list(divisor_generator(n))
    divisors.pop(len(divisors)-1) #we're not including the number itself
    divisors=list(set(divisors)) #and we have to deal with duplicates 
    sumr=sum(divisors)
    if sumr > n:
        return 1
    elif sumr == n:
        return 2
    elif sumr < n:
        return 0
    else:
        return None

def generate_abundant():
    num=0
    while(num<=28123):#all numbers over 28123 can be found by adding two abundants
        num+=1
        while(is_abundant(num) != 1):
            num+=1
        yield num

def sum_all_non_abunds():
    abunds=list(generate_abundant())#get all abundant numbers under limit
    addedtwo=[]
    for i in abunds: #add every combination together
        for j in abunds:
            added= i+j
            if added<=28123: #only interested in less than 28123 above all are true
                addedtwo.append(added)
   
    addedtwo=set(addedtwo)
    ints=set(range(28124))
    running_sum=0
    
    for i in ints:
        if i not in addedtwo:
            running_sum+=i
    print(running_sum)

sum_all_non_abunds()
assert(is_abundant(12)==1)
assert(is_abundant(28)==2)
assert(is_abundant(5)==0)
