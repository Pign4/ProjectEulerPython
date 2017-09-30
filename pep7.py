# What is the 10 001st prime number?

from math import log
import numpy as np
import time

# pure python version
def primes(n):
    sieve = [True] * (n//2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def primes3to(n):
    sieve = np.ones(n//2, dtype=np.bool)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i//2]:
            sieve[i*i//2 :: i] = False
    return 2 * np.nonzero(sieve)[0][1::] + 1

def nth_prime(n):
    if type(n) != int or n < 1: return "Error!"
    elif n == 1: return 2
    else:
        # n*log(n) + n*log(log(n)) is the approximate upper limit for for the nth prime
        return primes3to(int(n*log(n) + n*log(log(n))))[n-2]

if __name__ == '__main__':
    start_time = time.time()

    print(nth_prime(10001))

    print("--- {} seconds ---".format(time.time() - start_time))
