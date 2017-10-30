# What is the sum of the digits of the number 2^1000?

import time

if __name__ == '__main__':
    start_time = time.time()

    n = 2 ** 1000
    print(sum(int(digit) for digit in str(n)))

    print("--- {} seconds ---".format(time.time() - start_time))
