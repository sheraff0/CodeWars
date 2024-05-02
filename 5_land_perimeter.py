def land_perimeter(arr):
    perimeter = 0
    n, m = len(arr), len(arr[0])
    for i in range(n):
        for j in range(m):
            if arr[i][j] == "X":
                for delta_i, delta_j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    try:
                        assert i+delta_i >= 0
                        assert j+delta_j >= 0
                        assert arr[i+delta_i][j+delta_j] == "X"
                    except:
                        perimeter += 1
    return f"Total land perimeter: {perimeter}"


if __name__ == "__main__":
    print(land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]))
