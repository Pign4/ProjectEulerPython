# How many such routes are there through a 20×20 grid?

import time
from math import factorial

def gridPaths(length, width):
    grid = [[1] + [0] * length] * (width + 1)
    grid[0] = [1] * (length + 1)
    for line in range(1, width + 1):
        for i in range(1, length + 1):
            grid[line][i] = grid[line - 1][i] + grid[line][i - 1]
    return grid[-1][-1]

if __name__ == '__main__':
    start_time = time.time()

    # GENERAL SOLUTIONS FOR RECTANGULAR GRIDS

    length = 20
    width = 20

    # programming solution (slower)
    print(gridPaths(length, width))

    # mathematical solution
    print(factorial(length + width) // (factorial(length) * factorial(width)))


    print("--- {} seconds ---".format(time.time() - start_time))
