# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import time

def py_triplet_sum(s):
    for a in range(3, s//3):
        a2 = a**2
        c = s - a - 1
        for b in range(2, a if 2*a < s//3 else s-2*a):
            c -= 1
            if a2 + b**2 == c**2:
                return a * b * c

if __name__ == '__main__':
    start_time = time.time()

    print(py_triplet_sum(1000))

    print("--- {} seconds ---".format(time.time() - start_time))
