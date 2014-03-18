#Find the largest three digit palindrome
#pretty easily to do the brute force method

possible=[]
answers=[]
for i in range (100,1000):
    for j in range(100,1000):
        possible.append(str(i*j))

for i in range(len(possible)):
    if possible[i]==possible[i][::-1]:
        answers.append(int(possible[i]))
        
print(max(answers))        
