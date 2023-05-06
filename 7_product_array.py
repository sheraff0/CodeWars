from math import prod


def product_array(numbers):
    product = prod(numbers)
    return [product / n for n in numbers]


if __name__ == "__main__":
    print(product_array([1,12,13]))
