def solve(game, only_min=True):
    _len = len(game)
    if _len == 0:
        return []
    n = int(game[0])
    if _len == n:
        return [(n,)]
    res = []
    for i in range(1, min(n + 1, _len)):
        s = int(game[i]) - i
        if s > 0:
            res += [(i,) + x for x in solve(str(s) + game[i+1:], only_min=only_min)]
    if not res:
        return res
    _min = min([len(x) for x in res])
    return sorted([x for x in res if not only_min or (len(x) == _min)])


if __name__ == "__main__":
    import sys
    game = str(sys.argv[1])
    print(solve(game, only_min=False))
