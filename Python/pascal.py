from math import sqrt


def pascal(n):
    step = 1
    start = 2

    # If n is odd, its divisors are also odd
    if n % 2 == 1:
        step = 2
        start = 3

    for i in range(start, int(sqrt(n)) + 1, step):
        if n % i == 0:
            return n - n // i

    return n - 1


N = int(input())
print(pascal(N))
