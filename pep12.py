# What is the value of the first triangle number to have over five hundred divisors?

import time
from math import ceil, sqrt

def nod(n, start):
    if n == 1:
        return 1
    for i in range(start, int(ceil(sqrt(n))) + 1):
        if n % i == 0:
            count = 1
            while(n % i == 0):
                n /= i
                count += 1
            return nod(n, i + 1) * count
    return 2

if __name__ == '__main__':
    start_time = time.time()

    howMany = 500
    d1 = 0
    d2 = 0
    i = 0
    while d1 * d2 <= howMany:
        i += 1
        if i % 2 == 0:
            d1 = nod(i // 2, 2)
        else:
            d2 = nod(i, 3)
    # given two coprimes numbers b and c
    # given a = b * c and p(x) = number of dividends of x
    # then p(a) = p(b) * p(c)
    # in our case:
    # a = the (i-1)th triangular number
    # b = i (if i is even, else i//2)
    # c = i - 1 (if i-1 is even, else (i-1) // 2)
    print(i * (i - 1) // 2)

    print("--- {} seconds ---".format(time.time() - start_time))
