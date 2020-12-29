HALF_AREA = 250 ** 2 / 4  # Area of half the triangle


def bazen(x, y):
    if (x, y) == (0, 0):
        x_res, y_res = 125, 125
    elif x == 250:
        x_res, y_res = 0, 125
    elif y == 250:
        x_res, y_res = 125, 0
    elif x == 0:
        x_res = 2 * HALF_AREA / (250 - y)
        if x_res > 250:
            x_res = 2 * HALF_AREA / y
            y_res = 0
        else:
            y_res = 250 - x_res
    elif y == 0:
        y_res = 2 * HALF_AREA / (250 - x)
        if y_res > 250:
            y_res = 2 * HALF_AREA / x
            x_res = 0
        else:
            x_res = 250 - y_res
    else:
        if x > y:
            x_res = 0
            y_res = 250 - 2 * HALF_AREA / x
        else:
            x_res = 250 - 2 * HALF_AREA / y
            y_res = 0

    return "%.2f %.2f" % (x_res, y_res)


X, Y = map(int, input().split())
print(bazen(X, Y))
