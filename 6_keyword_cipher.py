from functools import reduce


def keyword_cipher(msg, keyword):
    symbols = [*map(chr, range(97, 97+26)), " "]
    cipher = reduce(
        lambda acc, curr: acc + ([curr] if curr not in acc else []), keyword, []
    ) + [
        *filter(lambda x: x not in keyword, symbols)
    ]
    cipher_map = dict(zip(symbols, cipher))
    return "".join(cipher_map[x] for x in msg.lower())


if __name__ == '__main__':
    print(keyword_cipher("alpha bravo charlie", "delta"))
