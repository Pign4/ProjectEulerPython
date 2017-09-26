# By considering the terms in the Fibonacci sequence
# whose values do not exceed four million,
# find the sum of the even-valued terms.

import time

def evenFiboSum(top):
    a = 0
    b = 2
    s = 0
    while b < top:
        s += b
        a, b = b, 4*b+a
    return s

if __name__ == '__main__':
    start_time = time.time()

    top = 4e6
    print(evenFiboSum(top))

    print("--- {} seconds ---".format(time.time() - start_time))
