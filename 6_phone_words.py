from functools import reduce

 
def phone_words(string_of_nums):
    return reduce(
        lambda acc, curr: acc.replace(*curr),
        [(n * i, letters[i-1])
            for n, letters in {
                '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz',
                '0': ' ',
            }.items()
            for i in range(len(letters), 0, -1)
        ] + [('1', '')],
        string_of_nums
    )


if __name__ == '__main__':
    print(phone_words('443355555566604466690277733099966688'))
