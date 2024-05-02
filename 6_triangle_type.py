# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle

def triangle_type(a, b, c):
    sides = (a, b, c)
    for i in range(3):
        x = sides[i]
        y, z = [sides[j] for j in range(3) if j != i]
        if x >= y + z:
            return 0
        delta = x**2 - y**2 - z**2
        if delta == 0:
            return 2
        if delta > 0:
            return 3
    return 1


if __name__ == "__main__":
    print(triangle_type(8,5,7))
