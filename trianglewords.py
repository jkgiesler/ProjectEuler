def word_to_number(word):
    x = 0
    for i in word:
        x += ord(i)-64
    return x




file_in = open('words.txt','rt')
listr = list()

for line in file_in: ##only a one line file
    line = line.rstrip()
    listr = line.split(",")

cleanedListr = list()
for i in listr:
    cleanedListr.append(word_to_number(i[1:len(i)-1]))

max_num=max(cleanedListr)
triNumbers = set()
i = 1
num = 1
while( num <= max_num):
    triNumbers.add(num)
    i += 1
    num = (i*(i+1)) / 2
solution = 0
for i in cleanedListr:
    if i in triNumbers:
        solution+=1

print(solution)
