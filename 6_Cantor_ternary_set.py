Fraction = tuple[int, int]
Interval = tuple[Fraction, Fraction]


def is_in_cantor(num, den, n):
    def remove_middle_third(interval: Interval) -> tuple[Interval, Interval]:
        a, b = interval
        den = 3 * a[1] * b[1]
        return ((a, (2 * a[0] * b[1] + b[0] * a[1], den)),
            ((a[0] * b[1] + 2 * b[0] * a[1], den), b))

    if not (0 <= num / den <= 1):
        return False

    Cn: list[Interval] = [((0, 1), (1, 1))]
    while n > 0:
        Cn = [y for x in Cn for y in remove_middle_third(x)]
        n -= 1
    return any(True for a, b in Cn if a[0] / a[1] <= num / den <= b[0] / b[1])


if __name__ == "__main__":
    for i in range(5):
        print(is_in_cantor(1, 2, i))
