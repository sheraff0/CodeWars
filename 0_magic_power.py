from math import log2
from multiprocessing import Pool
import time


def evaluate_range(i):
    for j in range(2, int(log2(i))+1):
        diff = sum(map(int, [*str(i)])) - j - i**(1/j)
        if max(diff, -diff) < 10**(-7):
            print(i, j)


def magic_power(N):
    t0 = time.time()
    with Pool(4) as p:
        p.map(evaluate_range, range(2, N))
    print(time.time() - t0)


if __name__ == '__main__':
    magic_power(10**6)
