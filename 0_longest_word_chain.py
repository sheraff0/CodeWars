from itertools import chain, combinations, permutations

# https://levelup.gitconnected.com/12-difficult-python-questions-you-might-take-days-to-solve-161bba5ad206


def all_chains(words):
    return (x for x in chain(*(permutations(x) for x in chain(*(combinations(words, i) for i in range(2, len(words) + 1)))))
        if all([x[j][-1] == x[j+1][0] for j in range(len(x) - 1)]))


def longest_word_chain(words):
    _chains = [*all_chains(words)]
    _max = max(len(x) for x in _chains)
    return [x for x in _chains if len(x) == _max]



if __name__ == '__main__':
    words = ["apple", "orange", "tank", "elephant", "kitten"]
    print(longest_word_chain(words))
