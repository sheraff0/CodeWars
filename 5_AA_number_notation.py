import re

letters = "abcdefghijklmnopqrstuvwxyz"
notations = ["", *"KMBT"] + [x + y for x in letters for y in letters]


def format_number(x):
    if search := re.search(r"^(-)?(\d+)(\.)?(\d+)?$", str(x)):
        sign, integer, dot, fraction = search.groups()
        _len = len(integer)
        rank = max(0, _len // 3 - (1 if _len % 3 == 0 else 0))
        sign_dot = None
    elif search := re.search(r"^(-)?(\d+)(\.)?(\d+)?e([+-])(\d+)$", str(x)):
        sign, integer, dot, fraction, sign_dot, _len = search.groups()
        _len = int(_len)
        rank = _len // 3
        integer = int(integer) * 10 ** (_len % 3)
        integer = str(integer)
        print(integer)
    notation = notations[rank]
    sign = sign or ""
    fraction = fraction or ""
    if rank > 0 and (not sign_dot):
        integer, fraction = integer[:-3*rank], integer[-3*rank:] + fraction
    n = max(0, 3 - len(integer))
    fraction = re.search(re.compile("([^0]{," + str(n) + "})\d*$"), fraction)
    fraction = fraction.groups()[0] if fraction else ""
    return sign + integer + ("." if fraction else "") + fraction + notation



if __name__ == "__main__":
    print(format_number(0.1))
    print(format_number(1230))
    print(format_number(1990))
    print(format_number(1234567890))
    print(format_number(-999999999999999))
    print(format_number(1234567890000000000))
    print(format_number(1.23456789e+17))
    print(format_number(-1.23456789e+25))
