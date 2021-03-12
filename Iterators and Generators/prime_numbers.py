def get_primes(integers):
    for prime in integers:
        if prime != 0 and prime != 1:
            if prime % 2 != 0 and prime % 3 != 0 and prime % 5 != 0 and prime % 7 != 0 and prime % 11 != 0:
                yield prime
            if prime in [2, 3, 5, 7, 11]:
                yield prime


# print(list(get_primes([23, 29, 31, 37, 41, 43, 47, 53])))
