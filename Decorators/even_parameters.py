def even_parameters(fn):
    def wrapper(*args):
        if len(args) == len([x for x in args if isinstance(x, int) and x % 2 == 0]):
            result = fn(*args)
            return result

        return "Please use only even numbers!"

    return wrapper


# @even_parameters
# def add(a, b):
#     return a + b
#
# print(add(2, 4))
# print(add("Peter", 1))
