'''
score a file filled with names by their rank and sum of their letters
'''


def dealingwfile():
    '''dealing with an ugly file'''
    namefile=open('names.txt','rt')
    strin=''
    for line in namefile:
        x=line.rstrip()
        strin+=x
    namefile.close()
    listr=strin.split(',')
    parsedl=[]
    for i in listr:
        parsedl.append(i[1:len(i)-1])
    return parsedl

def char_position(name):
    '''calculate the score of a word where a=1, b=2, c=3'''
    ans=0    
    for i in name:
        ans+=(ord(i)-64)
    
    return ans
    
def calculate_file_score():
    parsedlist=dealingwfile()
    parsedlist.sort()
    final=0
    for i in range(len(parsedlist)):
        count=0
        for j in parsedlist[i]:
            #calculate the word score and multiply it by position
            count+=char_position(j)*(i+1)
        
        final+=count
    print(final)

calculate_file_score()