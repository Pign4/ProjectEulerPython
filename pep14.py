# Which starting number, under one million, produces the longest chain?

# import time
#
# def recursive_collatz(n):
#     if n not in collatz_map:
#         if n % 2 == 0:
#             collatz_map[n] = 1 + recursive_collatz(n // 2)
#         else:
#             collatz_map[n] = 2 + recursive_collatz((3 * n + 1) // 2)
#     return collatz_map[n]
#
# if __name__ == '__main__':
#     start_time = time.time()
#
#     collatz_map = {1:1}
#
#     largest_so_far = 1
#     highest = 0
#     for i in range(2, 1000000):
#         temp = recursive_collatz(i)
#         if temp > largest_so_far:
#             highest = i
#             largest_so_far = temp
#     print(largest_so_far, highest)
#
#     print("--- {} seconds ---".format(time.time() - start_time))

import time
from math import log

def recursive_collatz(n):
    if n >= limit:
        if n not in collatz_map:
            if n % 2 == 0:
                collatz_map[n] = 1 + recursive_collatz(n // 2)
            else:
                collatz_map[n] = 2 + recursive_collatz((3 * n + 1) // 2)
        return collatz_map[n]
    else:
        if not collatz_list[n]:
            if n % 2 == 0:
                collatz_list[n] = 1 + recursive_collatz(n // 2)
            else:
                collatz_list[n] = 2 + recursive_collatz((3 * n + 1) // 2)
        return collatz_list[n]

if __name__ == '__main__':
    start_time = time.time()

    limit = 1000000
    collatz_list = [0] * limit
    # collatz_list[1] = 1
    collatz_map = {}

    largest_so_far = 1
    highest = 0
    l = int(log(limit, 2)) + 1
    for x in range(l):
        collatz_list[2**x] = x + 1
    # collatz_list[slice(2**x for x in range(l))] = [x + 1 for x in range(l)]
    for i in range(3, limit):
        temp = recursive_collatz(i)
        if temp > largest_so_far:
            highest = i
            largest_so_far = temp
    print(largest_so_far, highest)

    print("--- {} seconds ---".format(time.time() - start_time))
