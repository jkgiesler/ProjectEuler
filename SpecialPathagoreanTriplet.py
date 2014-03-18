from math import *
'''
find a b c for a^2+b^2=c^2 and a+b+c=1000
'''


for a in range(1000):
    for b in range(1000):
        if math.sqrt(a**2+b**2)+a+b==1000:
            c=(1000-(a+b))
            if (a**2+b**2==c**2):
                print([a,b,c])
                print(a*b*c)
        