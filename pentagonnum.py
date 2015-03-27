pentagons = set([(n*(3*n-1))/2 for n in range(1,10001)])

def is_pentagon(n):
    return n in pentagons
  
for i in pentagons:
    for j in pentagons:
        if is_pentagon(i+j) and is_pentagon(i-j):
            print(i,j)
            

    



        

