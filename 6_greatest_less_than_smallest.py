def divisible(x, y, m):
    return m % x == 0 and m % y == 0


def get_result(x, y, n, step, condition):
    m = n + step
    while condition(m):
        if divisible(x, y, m):
            break
        m += step
    return m


def greatest(x, y, n):
    return get_result(x, y, n, -1, lambda m: m > 0)


def smallest(x, y, n):
    return get_result(x, y, n, 1, lambda m: True)


if __name__ == "__main__":
    print(greatest(10,100,100))
    print(smallest(10,100,100))
