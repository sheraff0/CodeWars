# https://www.codewars.com/kata/526233aefd4764272800036f
 
def matrix_addition(a, b):
    return [[*map(sum, zip(*x))] for x in zip(a, b)]


if __name__ == "__main__":
    print(matrix_addition(
        [ [1, 2, 3],
            [3, 2, 1],
            [1, 1, 1] ],
        #       +
        [ [2, 2, 1],
            [3, 2, 3],
            [1, 1, 3] ]
    ))
