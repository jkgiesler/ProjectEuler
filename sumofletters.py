"""
add up all of the letters in
the numbers 1 through 1000
make sure to put ands in there
"""
numlist=[]
listofnumbers=open('wordlist.txt','rt')
for line in listofnumbers:
    line=line.rstrip()
    numlist.append(line)
listofnumbers.close()

#find number of letters in 1-20
letters1to20=[]
for i in range(20):
    #print(numlist[i])
    letters1to20.append(numlist[i])

teens=numlist[9:19]
#dump silly numbers
for i in range(10):
    print(numlist.pop(9)) #get rid of 9th index a lot
 
   
#print(numlist)
ones=numlist[0:9]
ones.insert(0,'')
tens=numlist[9:]


#find numbers 20-99
letters2099=[]
for i in range(len(tens)):
    for j in range(len(ones)):
        letters2099.append(tens[i]+ones[j])

#letters2099-=6 #forgot to get rid of duplicate 'twenty'

letters100120=[]
#find numbers x00-x20
lowernums=ones+teens
for i in range(len(ones)):
    for j in range(len(lowernums)):
        if i==0:
            pass
        elif j==0:
            letters100120.append(ones[i]+'hundred'+lowernums[j])
        else:
            letters100120.append(ones[i]+'hundredand'+lowernums[j])



#findnumbers 120-999
letters100999=[]
    
for i in range(len(tens)):
    for j in range(len(ones)-1):
        for z in range(len(ones)):
            letters100999.append(ones[j+1]+'hundred'+'and'+tens[i]+ones[z])
            
z=set(letters1to20+letters2099+letters100120+letters100999+['onethousand'])
z=list(z)

sumr=0
for i in z:
    sumr+=len(i)