# https://www.codewars.com/kata/63744cbed39ec3376c84ff4a
 
import re
from functools import reduce

MATCHES = (
    (r'<=+>', 0),
    (r'<-*>', 0),
    (r'=+>', 2),
    (r'-*>', 1),
    (r'<=+', -2),
    (r'<-*', -1),
)


def arrow_search(string: str) -> int:
    def re_list(pattern, strings, func):
        return [x for s in strings for x in func(pattern, s)]

    res = 0
    strings = [string]
    for pattern, score in MATCHES:
        matches = re_list(pattern, strings, re.findall)
        res += score * len(''.join(matches))
        strings = re_list(pattern, strings, re.split)
    return res


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('string', type=str)
    args = parser.parse_args()
    res = arrow_search(args.string)
    print(res)