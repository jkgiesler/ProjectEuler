def returndivisors(n):
    '''looks for a suitably large factor'''    
    divisors=0    
    for x in range(1,int(n**.5)+1):
        if n%x==0:
            divisors+=2
    return divisors

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
    
    print(n,'has ',test,'divisors')
    n=next(z)

    