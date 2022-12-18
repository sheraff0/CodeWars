# https://www.codewars.com/kata/54c9fcad28ec4c6e680011aa/train/python


def is_merge(s, p1, p2):
    def check(p):
        s_ = s
        i = 0
        for letter in p:
            try:
                i = s_.index(letter, i)
                s_ = s_[:i] + s_[i+1:]
            except ValueError:
                return False
        return True

    return all([
        *map(check, [p1, p2]),
        sorted(s) == sorted(p1 + p2)
    ])


if __name__ == "__main__":
    print(is_merge(
        "5!MKFKedS  $", "!MKed", "5KFS  $"
    ))
