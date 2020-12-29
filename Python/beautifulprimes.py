from math import log10


def beautifulprimes(n):
    primes = [3, 5, 7]  # We'll only need primes <= 11, as the biggest number with n digits is 10**n - 1
    combination = [11] * n  # We start from the biggest combination possible, this will be useful for big values of n
    nb_digits = sum(log10(i) for i in combination) + 1

    for i in range(n):
        k = 0

        while k < 3 and int(nb_digits) != n:
            nb_digits -= log10(combination[i])
            combination[i] = primes[2-k]
            nb_digits += log10(combination[i])

            k += 1

    return combination


T = int(input())
for _ in range(T):
    N = int(input())
    print(*beautifulprimes(N))
