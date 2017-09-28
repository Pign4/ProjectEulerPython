# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time

# Smallest Number Divisible by Range of
def SNDR(n):
    product = 1
    dividends = []
    for i in range(2,n+1):
        for div in dividends:
            if i % div == 0:
                i //= div
        dividends.append(i)
        product *= i
    return product

if __name__ == '__main__':
    start_time = time.time()

    n = 20
    print(SNDR(n))

    print("--- {} seconds ---".format(time.time() - start_time))
