# https://www.codewars.com/kata/635f67667dadea064acb2c4a/train/python

CREW = {"F": "Frank", "S": "Sam", "T": "Tom"}
NON_WATER_PROOF = [*CREW, ' ', 'x']


class Flotsam:
    def __init__(self, pic):
        self.pic = pic
        self.sea_level = next(i for i, x in enumerate(pic) if '~' in x)
        self.bottom = len(self.pic)
        self.width = len(self.pic[0])
        self.survivors = dict(**CREW)

    def show(self):
        print("\n".join(["".join(row) for row in self.pic]))

    def drown(self, person):
        name = self.survivors.pop(person)
        print(f"{name} drowned!")

    def leak(self, i1, j1, i2, j2) -> bool:
        a, b = self.pic[i1][j1] , self.pic[i2][j2]
        if a == '~' and b in NON_WATER_PROOF:
            if b in self.survivors:
                self.drown(b)
            self.pic[i2][j2] = '~'
            return True
        else:
            return False

    def sink(self):
        leaked = False
        for i in range(self.sea_level, self.bottom):
            for direction in (1, -1):
                for j in [*range(self.width)][::direction]:
                    if j < self.width - 1:
                        leaked |= self.leak(i, j, i, j+1)
                        leaked |= self.leak(i, j+1, i, j)
                    if i > self.sea_level:
                        leaked |= self.leak(i, j, i-1, j)
                    if self.sea_level <= i < self.bottom - 1:
                        leaked |= self.leak(i, j, i+1, j)
        self.show()
        if leaked and self.survivors:
            print(self.survivors)
            self.sink()


def flotsam(pic):
    o = Flotsam(pic)
    o.show()
    o.sink()
    result = " ".join(o.survivors.values())
    return(result)


if __name__ == "__main__":
    flotsam([[*x] for x in """          |==|  |==|  |==|          
        __|__|__|__|__|__|_         
     __|___________________|___     
  __|__[]__[]__[]__[]__[]__[]__|_xx 
~x                                /~
~|                                /~
~|                                /~
~|                                /~
~|                                /~
~|      F  x  S    x  T           |~
~|______|_______|________________/~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""".split('\n')])
