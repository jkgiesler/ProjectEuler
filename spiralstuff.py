'''
calculate the sum of a 1001 by 1001 spiral
which is along these lines
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
'''

count=1
lst_str=[]

for i in range(2,200000000000000,2):
    for j in range(4):
        lst_str.append(count)
        count+=i
        if len(lst_str)==2001:
            break
    if len(lst_str)==2001:
        break
print(sum(lst_str))