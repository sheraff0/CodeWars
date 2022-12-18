def number_joy(n):
    sum_digits = sum(map(int, [*str(n)]))
    sum_digits_reverse = int(str(sum_digits)[::-1])
    return n == sum_digits * sum_digits_reverse


if __name__ == '__main__':
    number_joy(81)
    number_joy(1729)
    number_joy(1458)
    print([*filter(number_joy, range(10**6))])
