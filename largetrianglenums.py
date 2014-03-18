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


def returndivisors(n):
    '''looks for a suitably large factor'''    
    divisors=[]    
    for x in range(2,int(n**.5)+1,1):
        if n%x==0:
            divisors.append(x)
    return len(divisors)

def generatetrianglenumbers():
    num = 0
    count =0
    while(True):
        num=0
        for x in range(count):
            num+=x
        count+=1
        yield num
        
z=generatetrianglenumbers()        
n=0
test=returndivisors(n)
while(test < 500):    
    test=returndivisors(n)
    
    print(n)
    n=next(z)

    