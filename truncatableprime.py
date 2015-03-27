'''
there are 11 prime numbers which remain
prime as you strip away all of the digits
from either side. Find them and sum them

ie: 3797
379 37 3   are all prime numbers
797 97 7 
'''
def isprime(n):
    '''checks if n is prime'''    
    n= abs(int(n))
    
    if n<2:
        return False
    if n==2:
        return True
    if not n & 1:
        return False
        
    for x in range(3,int(n**.5)+1,2):
        if n%x==0:           
            return False
            
    return True

def truncatable(n):
    right_to_left = str(n)
    left_to_right = str(n)
    while len(right_to_left)>1:
        right_to_left=right_to_left[1:]
        left_to_right = left_to_right[:-1]
        if not isprime(int(right_to_left)) \
            or not isprime(int(left_to_right)):
            return False
    return True


def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]


eleven=[]
x=sieve_for_primes_to(10000000)
x=x[4:]

for i in x:
    if truncatable(i):
        eleven.append(i)
        if len(eleven)==11:
            break
print(eleven)
print(sum(eleven))