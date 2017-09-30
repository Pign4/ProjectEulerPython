# Find the sum of all the primes below two million

import time
from pep7 import primes3to

def sumSE(n):
	if n < 2: return 0
	return 2 + sum(primes3to(n))

if __name__ == '__main__':
    start_time = time.time()

    print(sumSE(2000000))

    print("--- {} seconds ---".format(time.time() - start_time))
