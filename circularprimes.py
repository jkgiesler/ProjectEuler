'''
find circular prime numbers ie 197, 971, 719
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

def check_all_combos(n):
    n=str(n)
    possibilities = []
    for i in range(len(n)):
        n = n[-1]+n[0:-1]
        possibilities.append(n)
    for i in possibilities:
        if not isprime(i):
            return False
    return True


def run():
    x=sieve_for_primes_to(1000001)
    success = []
    for i in x:
        if check_all_combos(i):
            success.append(i)
    print(success)
    print(len(success))

