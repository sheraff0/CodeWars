import re


def kooka_counter(laughing):
    return re.findall("(Ha)+|(ha)+", laughing)


if __name__ == '__main__':
    print(kooka_counter("HaHaHahahaHaHa"))