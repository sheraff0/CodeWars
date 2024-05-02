def all_squared_pairs(n):
    top = int(n ** .5)
    return [[i, j] for i in range(top+1) for j in range(i, top+1)
        if i*i + j*j == n]


if __name__ == "__main__":
    print(all_squared_pairs(500000))
