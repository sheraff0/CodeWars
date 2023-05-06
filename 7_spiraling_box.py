def create_box(m, n):  ## m and n positive integers
    res = [
        [min(j+1, m-j, i+1, n-i) for j in range(m)]
        for i in range(n)
    ]
    print(res)
    return res


if __name__ == '__main__':
    create_box(5, 8)
