def decode(code, key):
    Z = ord("a") - 1
    key_ = str(key)
    len_ = len(key_)
    return "".join(chr(Z + x - int(key_[i % len_]))
        for i, x in enumerate(code))


if __name__ == "__main__":
    print(decode([14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8], 1939))
