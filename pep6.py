# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.

from pep1 import range_sum
import time

def range_sum_squares(x):
    return x * (x + 1) * (2 * x + 1) // 6

if __name__ == '__main__':
    start_time = time.time()

    n = 100
    print(range_sum(n)**2 - range_sum_squares(n))

    print("--- {} seconds ---".format(time.time() - start_time))
