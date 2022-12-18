# https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111/train/python

from functools import reduce


def triangle(row):
    def sieve(pair):
        if pair[0] == pair[1]:
            return pair[0]
        return list(set('RGB') - set(pair))[0]

    while len(row) > 1:
        row = reduce(lambda acc, i:
            acc + sieve(row[i:i+2]), range(len(row) - 1), '')
    return row


if __name__ == '__main__':
    print(triangle('RGBBGR'))
