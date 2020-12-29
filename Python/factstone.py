from math import log2

# We'll determine the adequate n for all the concerned range of years
bits_per_year = {v: 2 ** (k + 2) for k, v in enumerate(range(1960, 2170, 10))}
n_per_year = {}

sum_log = 1
year = 1960
n = 3

while year <= 2160:
    sum_log += log2(n)

    if sum_log >= bits_per_year[year]:  # This comes from developing the expression: n! < 2 ** bits
        n_per_year[year] = n-1
        year += 10

    n += 1

while True:
    year = int(input())
    if year == 0:
        break

    decade = round(year // 10) * 10
    print(n_per_year[decade])
