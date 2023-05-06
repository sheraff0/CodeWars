def real_numbers(n):
    res = n - sum(n//k for k in (2,3,5,30)) + sum(n//k for k in (6,10,15))
    print(res)
    return res


if __name__ == "__main__":
    real_numbers(66)
