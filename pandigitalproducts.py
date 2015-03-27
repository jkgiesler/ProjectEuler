
'''
find all number whose two divisors and the number contain all
123456789
'''


import math

def divisor_generator(n):
    '''
    returns all divisors including n and in some cases duplicates
    be careful
    '''
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors:
        yield int(divisor)

def get_divisor_tuples(n):
    ls=list(divisor_generator(n))
    end_ls = []
    for i in range(int(len(ls)/2)):
        end_ls.append(tuple([ls[i], ls[-i -1]]))
    return tuple(end_ls)

def check_pandigital(n):
    count_dict={}
    check=str(n)
    success=[]
    for i in check:
        if i in count_dict.keys():
            return success
        else:
            count_dict[i]=1
    tuples = get_divisor_tuples(n)
    for i in tuples:
        check_count_dict = count_dict.copy()
        div1 = str(i[0])
        div2 = str(i[1])
        for j in div1:
            if j in check_count_dict:
                check_count_dict[j]+=1
            else:
                check_count_dict[j]= 1
        for j in div2:
            if j in check_count_dict:
                check_count_dict[j]+=1
            else:
                check_count_dict[j]=1

        if len(check_count_dict.keys()) == 9 and max(check_count_dict.values())==1:
            success.append(i)
    return success


def check_all():
    success_set=set()
    for i in range(987654321):
        if len(check_pandigital(i)) > 0:
            success_set.add(i)
    print(sum(success_set))

    return

