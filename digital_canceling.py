'''
There are 4 fractions of 2 digit numbers which allow for 
incorrect cancelation. Find them and then multiply them together
and find the denominator in the most reduced form

ie 16/64 = 1/4

'''




ilst=[]
jlst=[]

for i in range(10,99):
  for j in range(10,99):
    if i/j <1:
      str_i = str(i)
      str_j = str(j)
      copies = []
      for x in str_i:
        for n in str_j:
          if x == n and x != '0' and n !='0':
            str_i = str_i.replace(x,'')
            str_j = str_j.replace(n,'')

            try:
              new_i = int(str_i)
              new_j = int(str_j)
              if new_i/new_j == i/j:
                ilst.append(i)
                jlst.append(j)

            except:
              pass
print(ilst)
print(jlst)

