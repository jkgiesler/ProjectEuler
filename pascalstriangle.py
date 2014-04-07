'''
generate n rows of pascals triangle
'''


def next(row):
  newrow = [ row[k-1]+row[k]
             for k in range(1,len(row)) ]
  return [1] + newrow + [1]
def pascal(rowsleft,oldrow):
  if rowsleft > 0:
    R = next(oldrow)
    print (R)
    pascal(rowsleft-1,R)
print ([1])
print ([1,2,1])
pascal(40,[1,2,1])


z=2**1000
sum=0
for i in str(z):
    sum+=int(i)
print(sum)