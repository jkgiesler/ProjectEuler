
'''
    Product of n-digit number and m-digit number will contain n+m-1 or n+m digits.
    Therefore n + m + (n + m - 1) = 9 or n + m + (n + m) = 9 => 
    => n + m = 5 and the product is 4-digit
'''

def is_pandigital(n, m):
    return len(str(n*m))==4 and \
           len("".join(set(str(n)+str(m)+str(n*m))).replace('0','')) == 9

print(sum(set(
      [n*m for n in range(1,10) for m in range(1234,9877) if is_pandigital(n, m)] +
      [n*m for n in range(12,99) for m in range(123,988) if is_pandigital(n, m)])))