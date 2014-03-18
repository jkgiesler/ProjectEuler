'''
this script tests Goldbach's second conjecture that every nonprime
odd number can be expressed as the sum of a prime and twice a square
it takes advantage of a pretty crudely implemented sieve to generate all
odd numbers from 2 to 10000. For some reason I assumend that the number
would fall between 0 and 10000. Set methods are really useful in this code.

'''
def generatelst():
    n=3
    biggest=15000
    lst=[]
    
    for i in range(2,12000):
        lst.append(i)
    return lst

def sieve(lst,n):
    '''returns only numbers in the list which are not divisible by n'''
    ans=[]
    for i in lst:
        if (i%n !=0 or i==n):
            ans.append(i)       
    return ans

def findprime():
    '''takes advantage of the sieve to generate all primes in the list'''
    z=generatelst()
    n=0
    npri=2
    tot=len(z)
    for i in range(2,tot):
        z=sieve(z,i)
    return z

def Goldbach():
    '''the script which searches for numbers which violate goldbach's second
    conjecture'''
    primes=findprime()
    
    odd=[]      
    for z in range(3,10001,2):
        odd.append(z)
        
    possibilities=[]
    
    for i in range(1,10000):
        for j in range(len(primes)):
            possibilities.append(primes[j]+(2*(i**2)))
    
    possibilities=set(possibilities)
    odd=set(odd)
    possibilities=odd-possibilities
    primes=set(primes)
    
    for i in possibilities:
        if i not in primes:
            print(i)
        