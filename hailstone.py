# Author: Paul Quaife
# Date: 1/27/2021
# Description: Hailstone Sequence

def hailstone(n):
    """Takes a positive integer as the initial number the hailstone sequence and returns how
    many steps it takes to reach 1"""
    count = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count
