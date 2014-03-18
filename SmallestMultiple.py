#what is the smallest positive number that is evenly divisible
#by all of the numbers from 1/20

def checkdivisors(n,divisors):    
    for i in divisors:
        if(not n%i==0):                      
            return False
            
    return True
def SmallestMultiple():
    '''
    find the smallest multiple which is evenly divisible by every number
    from 1 to 20
    '''
    divisors=list(range(1,21))
    count=len(divisors)
    startpoint=count
    condition=True
    
    while(condition):
        if(checkdivisors(startpoint,divisors)):
            print(startpoint)
            condition=False
        else:
            startpoint+=count

math.log(n)+math.log(math.log(n-1))+(math.log(math.log(n-2))/math.log(n))