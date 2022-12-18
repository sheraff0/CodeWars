def find_nb(m):
    i = 1
    s = 1
    while s <= m:
        if s == m:
            return i
        i += 1
        s += i**3
    return -1


if __name__ == "__main__":
    import sys
    try:
        num = int(sys.argv[1])
        print(find_nb(num))
    except IndexError:
        print("Enter number!")
    except ValueError:
        print("Wrong input number!")
