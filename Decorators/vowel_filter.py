def vowel_filter(function):
    def wrapper():
        return [vowel for vowel in function() if vowel.lower() in "aeiouy"]

    return wrapper

# @vowel_filter
# def get_letters():
#     return ["a", "b", "c", "d", "e"]


# print(get_letters())
