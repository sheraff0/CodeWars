import re


def decipher_this(s):
    matches = re.findall("((\d+)(\S*))+", s)
    res = ' '.join(chr(int(first)) + (
        f"{rest[-1]}{rest[1:-1]}{rest[0]}"
        if len(rest) > 1 else rest
    ) for _, first, rest in matches)
    print(res)
    return res
    


if __name__ == '__main__':
    decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka")
    decipher_this("84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare")