#Problem 3###
#find the largest prime factor of 600851475143

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
    return max(divisors)

def problem3():
    divisors=[]
    num=600851475143
    divisors.append(num)
    nonprime=True
    while(nonprime):
        z=range(len(divisors))
        for i in z:
            testcase=divisors[i]
            if not (isprime(testcase)):
                divisors.pop(i)
                divint=returndivisors(testcase)
                ans=int(testcase/divint)
                divisors.append(divint)
                divisors.append(ans)
        
        sumnoprime=0
        for i in divisors:
            if not isprime(i):
                sumnoprime+=1
        if sumnoprime==0:
            nonprime=False
    
    print(max(divisors))