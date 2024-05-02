def get_count(n):
    s = str(n)
    len_ = len(s)
    return sum(1 for i in range(len_)
        for j in range(i + 1, len_ + 1)
        if (x := int(s[i:j])) and (x > 0) and n % x == 0
    ) - 1


if __name__ == "__main__":
    print(get_count(1230))
    print(get_count(1111111111))
