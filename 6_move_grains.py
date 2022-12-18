# https://www.codewars.com/kata/628d1c71b091df00651f0d83/train/python
from math import ceil, floor


def move_grains(grains):
    def avg(list_):
        return sum(list_) / len(list_)

    min_, max_, avg = [tuple(map(func, [[x[i] for x in grains] for i in (0, 1)]))
        for func in (min, max, avg)]
    avg_ = set(((func1(avg[0]), func2(avg[1])) for func1 in (floor, ceil) for func2 in (floor, ceil)))
    res = []
    moves = 10**9
    for i, j in avg_:
        moves_ = sum((abs(x[0]-i) + abs(x[1]-j) for x in grains))
        if moves_ == moves:
            res.append((i, j))
        elif moves_ < moves:
            res = [(i, j)]
            moves = moves_
    return res


if __name__ == "__main__":
    res = move_grains({(1,3), (2,1), (4,3)})
    print(res)
