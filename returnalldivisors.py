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

print(list(divisor_generator(12)))