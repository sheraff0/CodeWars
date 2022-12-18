from functools import reduce

BASE = 300
N = 3
FACTOR = 0.8


def egged(year, span):
    if year == 0:
        return "No chickens yet!"
    return sum(reduce(lambda acc, curr:
        [N * BASE] + [int(x / N * FACTOR) * N for x in acc[:span-1]],
        range(year), []
    ))


if __name__ == "__main__":
    for year, span in ((0, 5), (2, 1), (4, 8), (74, 10), (1, 15)):
        print(year, span, egged(year, span))
