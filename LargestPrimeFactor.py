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


##quick and dirty solution to Question 7####
##which is the 10001 prime number
#assuming -2 because a loss of 2 and an indexing issue
def questoin8():
    num=10001
    stor=[]
    i=3
    while(len(stor)<10003):
        if isprime(i):
            stor.append(i)
        i+=2
    print(stor[9999])

###quick and dirty solution to question 9######
sumr=0
for i in range(2000000):
    if(isprime(i)):
        sumr+=i
print(sumr)
