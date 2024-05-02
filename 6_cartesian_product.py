def cart_prod(*sets):
    res = {()}
    for set_ in sets:
        res = {a + (b,) for a in res for b in set_}
    return res


if __name__ == "__main__":
    print(cart_prod(
        {1, 2},
        {2, 3, 4},
        {55, 77, 99, 111},
    ))
