def ip_to_int32(ip):
    #return sum(int(x) * 2**(8 * (3-i)) for i, x in enumerate(ip.split(".")))
    return sum(int(x) << 8 * (3-i) for i, x in enumerate(ip.split(".")))


if __name__ == '__main__':
    print(ip_to_int32("128.114.17.104"))
