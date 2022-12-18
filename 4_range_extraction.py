def solution(args):
    res = str(args[0])
    range_start = None
    for a, b in zip(args, args[1:]):
        if b - a > 1:
            if range_start:
                res += '-' if a - range_start > 1 else ','
                res += str(a)
            res += f',{str(b)}'
            range_start = None
        else:
            if range_start is None:
                range_start = a
    if range_start:
        res += '-' if b - range_start > 1 else ','
        res += str(b)
    return res


if __name__ == "__main__":
    print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
