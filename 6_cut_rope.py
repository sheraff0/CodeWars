from collections import Counter

def cut_rope(length, m, n):
    marks = set(range(0, length, m)) | set(range(0, length, n)) | {length}
    marks = sorted(list(marks))
    deltas = (y - x for x, y in zip(marks, marks[1:]))
    counter = {f"{k}cm": v for k, v in Counter(deltas).items()}
    print(counter)
    return counter

if __name__ == '__main__':
    cut_rope(19, 6, 6)