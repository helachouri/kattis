def creditcard(r, b, m):
    for i in range(1, 1201):
        interest = round(r * b) / 100  # Rounding to the nearest cent
        b = round((b + interest) * 100) / 100
        b -= m

        if b < 1e-3:
            return i

    return "impossible"


T = int(input())
for _ in range(T):
    R, B, M = map(float, input().split())
    print(creditcard(R, B, M))
