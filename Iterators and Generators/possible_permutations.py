from itertools import permutations


def possible_permutations(numbers):
    all_permutations = permutations(numbers)

    for permutation in all_permutations:
        yield list(permutation)


# [print(n) for n in possible_permutations([1, 2, 3])]
