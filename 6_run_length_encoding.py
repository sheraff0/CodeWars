import re


def encode(string):
    return re.sub(r"(.)\1*", lambda m: str(len(m.group(0))) + m.group(1), string)


def decode(string):
    return re.sub(r"(\d)(\D)", lambda m: int(m.group(1)) * m.group(2), string)



if __name__ == "__main__":
    print(encode("AAABBBCCCA"))
    print(decode("3A3B3C1A"))
