# Find the largest palindrome made from the product of two 3-digit numbers.

import time

def product_2_n_digit(n, i, M, m):
    for j in range(M-1,m,-1):
        if i % j == 0:
            if len(str(i//j)) == n:
                return True
    return False

# Conditional Largest Palindrome
def CLP(n):
    M = 10**n
    m = 10**(n-1)
    for i in range((M-1)**2,m**2,-1):
        string = str(i)
        if string == string[::-1]:
            if product_2_n_digit(n, i, M, m):
                return i

# # This version is faster but it only works if the largest palindrome is 2*n digits long.
# def largest_palindrome(n):
#     M = 10**n
#     m = 10**(n-1)
#     for i in [int(str(x)+str(x)[::-1]) for x in range(M - 1, m - 1, -1)]:
#         for j in range(M-1,m,-1):
#             if i % j == 0:
#                 if len(str(i//j)) == n:
#                     return i

if __name__ == '__main__':
    start_time = time.time()

    print(CLP(3))

    print("--- {} seconds ---".format(time.time() - start_time))
