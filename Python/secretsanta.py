def secretsanta(n):
    """
        P(One or more gift themselves) = 1 - P(No one gifts itself)
        There's n! possibilities in total
        There's !n combinations where no one picks his name
        P(No one gifts itself) = !n / n! = ∑(-1)^i / i! (i = 0 to n)
        !n denotes the number of derangements of a set of n elements, also called subfactorial n
    """

    n = min(n, 1000)  # Solution converges for large n to: 1 - 1 / e, because e^x = ∑x^i / i! (i = 0 to ∞)

    probability = 1
    factorial = 1
    for i in range(2, n+1):
        factorial *= i

        if i % 2 == 0:
            probability -= 1 / factorial
        else:
            probability += 1 / factorial

    return probability


N = int(input())
print(secretsanta(N))
