# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

from itertools import combinations
from functools import reduce
from operator import mul
import time

def range_sum(x):
    return x * (x + 1) // 2

# Sum All Multiples - one dividend
def SAMod(div, top):
    ''' E.g. SAMod(3, 10)
    -> x = 10//3 = 3
    -> return 3 * 3 * (3+1) // 2 = 18
    in fact 3 + 6 + 9 (the only multiples of 3 below 11) = 18
    '''
    x = top // div
    return div * range_sum(x)

# Sum All Multiples - multiple dividends
def SAMmd(divs, top):
    """ Returns the sum of all mutiples of l numbers below top + 1 """
    l = len(divs)
    if l == 0: return 0
    s = sum(SAMod(div, top) for div in divs)
    for comb in [comb for r in range(2, l+1) for comb in combinations(divs, r)]:
        # subtracts from s the sum of all the multiples
        # of the product of the numbers inside comb,
        # where comb is any combination of two or more numbers in divs.
        s -= SAMod(reduce(mul, list(comb)), top)
    return s

if __name__ == '__main__':
    start_time = time.time()

    top = 999 # because it must be 'all the multiples BELOW 1000.'

    # first solution
    print(SAMod(3, top) + SAMod(5, top) - SAMod(15, top))

    # general solution
    print(SAMmd([3,5], top))

    print("--- {} seconds ---".format(time.time() - start_time))
