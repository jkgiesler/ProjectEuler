'''
n**2+n+41 is prime for 0 to 39
n**2+n+80 is prime n=0 to 79
find a*b such that a and b produce the most primes
'''


def is_prime(n):
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

def find_best_solution():
    maxcount=0
    a=0
    b=0
    for i in range(2001):
        for j in range (2001):
            n=0
            ans=(n**2+((i-1000)*n)+j-1000)
            while(is_prime(ans)):
                n+=1
                ans=(n**2+((i-1000)*n)+j-1000)
                
            if n>maxcount:
                maxcount=n
                a=i-1000
                b=j-1000
    print(a*b)
            
find_best_solution()