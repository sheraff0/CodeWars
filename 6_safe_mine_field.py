DIRECTIONS = {
    (-1, 0): "North",
    (1, 0): "South",
    (0, 1): "East",
    (0, -1): "West"
}


class SafeMineField:
    def __init__(self, mine_field):
        self.mine_field = mine_field

    def show(self):
        print("\n".join(["".join(row) for row in self.mine_field]))
        print()

    def explode_direction(self, i, j, v):
        k = 1
        while True:
            try:
                p, q = i + k*v[0], j + k*v[1]
                assert p >= 0
                assert q >= 0
                assert self.mine_field[p][q] not in 'TM'
                self.mine_field[p][q] = 'C'
                k += 1
            except:
                break

    def explode(self, i, j):
        for v in DIRECTIONS:
            self.explode_direction(i, j, v)

    def locate_all(self, symbol):
        return [(i, j)
            for i, row in enumerate(self.mine_field)
            for j, x in enumerate(row)
            if x == symbol
        ]

    def __call__(self):
        for i, j in self.locate_all('M'):
            self.explode(i, j)
            self.show()
        result = self.locate_all('.')
        return result


def safe_mine_field(mine_field):
    return SafeMineField(mine_field)()


if __name__ == "__main__":
    result = safe_mine_field([
            ['.', '.', 'T', '.', '.', '.', 'M'],
            ['.', 'T', '.', '.', '.', 'M', '.'],
            ['.', '.', 'M', '.', 'M', '.', '.'],
            ['.', 'M', '.', '.', '.', 'T', '.'], 
            ['M', '.', '.', '.', 'T', '.', '.']
        ])
    print(result)
