VALID_DIGITS = {"B": "8", "G": "C", "I": "1", "O": "0", "Q": "0", "S": "5", "U": "V", "Y": "V", "Z": "2"}
DECIMAL_MAPPING = {v: k for k, v in enumerate("0123456789ACDEFHJKLMNPRTVWX")}
COEFS = [2, 4, 5, 7, 8, 10, 11, 13]


def fbiuniversal(dataset):
    k, digits = dataset.split()
    ucn = digits[:-1]
    check_digit = DECIMAL_MAPPING[digits[-1]]

    for key, value in VALID_DIGITS.items():
        ucn.replace(key, value)

    ucn = list(ucn)
    check_sum = 0
    decimal_value = 0

    for i in range(8):
        check_sum += COEFS[i] * DECIMAL_MAPPING[ucn[i]]
        decimal_value *= 27
        decimal_value += DECIMAL_MAPPING[ucn[i]]

    if (check_sum % 27) == check_digit:
        return f"{k} {decimal_value}"

    return f"{k} Invalid"


P = int(input())
for _ in range(P):
    line = input()
    print(fbiuniversal(line))
