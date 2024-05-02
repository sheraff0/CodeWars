def zoom(n):
    def coat(s):
        nonlocal res
        res = [s + x + s for x in res]
        n = len(res[0])
        res = [s * n] + res + [s * n]

    res = ['■']
    color = 0
    while n > 1:
        coat('□■'[color])
        n -= 2
        color = (color + 1) % 2
    return "\n".join(res)


if __name__ == "__main__":
    print(zoom(1))
    print(zoom(3))
    print(zoom(5))
    print(zoom(7))
    print(zoom(9))
    print(zoom(11))
