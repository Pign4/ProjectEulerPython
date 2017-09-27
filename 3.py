# What is the largest prime factor of the nber 600851475143 ?

import time

# Largest Prime Factor
# def LPF(n):
#     if type(n) != int or n < 2: return "No prime divisors"
#     i = 2
#     while n % i == 0:
#         n /= i
#     if n > 1:
#         i += 1
#         while n > 1:
#             if n % i == 0: n /= i
#             else: i += 2
#     return i

# Faster version thanks to lack of modulo operations
def LPF(n):
    if type(n) != int or n < 2: return "No prime divisors"
    i = 2
    while True:
        x = n // i
        if x*i == n: n = x
        else: break
    if n > 1:
        i += 1
        while n > 1:
            x = n // i
            if x*i == n: n = x
            else: i += 2
    return i

if __name__ == '__main__':
    start_time = time.time()

    n = 600851475143
    print(LPF(n))

    print("--- {} seconds ---".format(time.time() - start_time))
