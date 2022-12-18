from collections import Counter


def first_non_repeating_letter(string):
    non_repeating = [k for k, v in Counter(string.lower()).items() if v == 1]
    for symbol in string:
        if symbol.lower() in non_repeating:
            return symbol
    return ''


if __name__ == "__main__":
    print(
        first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!')
    )
