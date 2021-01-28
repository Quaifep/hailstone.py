# Author: Paul Quaife
# Date: 1/27/2021
# Description: Hailstone Sequence

def hailstone(n):
    """Takes a positive integer as the initial number the hailstone sequence and returns how
    many steps it takes to reach 1"""
    count = 0  # number of steps to 0
    while n != 1:  # as long as n is not 1
        if n % 2 == 0:  # if n is even
            n //= 2
        else:
            n = 3 * n + 1
        count += 1  # increase number of steps by 1
    return count  # return the number of steps it took
