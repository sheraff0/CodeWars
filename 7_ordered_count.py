# https://www.codewars.com/kata/57a6633153ba33189e000074

from functools import reduce


def ordered_count(inp):
    return [(k, v) for k,v in reduce(lambda acc, curr:
        {**acc, curr: acc.get(curr, 0) + 1}, [*inp], {}).items()]


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("inp", type=str)
    args = parser.parse_args()
    res = ordered_count(args.inp)
    print(res)
