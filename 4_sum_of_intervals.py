# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

def sum_of_intervals(intervals):
    intervals_ = [*map(list, intervals)]
    res = [intervals_[0]]
    for a in intervals_[1:]:
        for i, r in enumerate(res):
            overlaps = False
            for j in (0, 1):
                if r[0] <= a[j] <= r[1]:
                    a[j] = r[j]
                    overlaps = True
            if a[0] <= r[0] <= r[1] <= a[1]:
                overlaps = True
            if overlaps:
                res[i] = [0, 0]
        res.append(a)
    return sum(y - x for x, y in res)


if __name__ == '__main__':
    print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
