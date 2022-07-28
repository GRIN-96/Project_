from functools import reduce

def solve(n):
    return reduce(lambda x, y : x+y , n)