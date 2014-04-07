'''
Get the millionth sorted iteration
'''

import itertools
x=list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))

listr=[]

for i in x:
   strg=''
   for y in i:
       strg+=str(y)
   listr.append(strg)

listr.sort()

print(listr[999999])