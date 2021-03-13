def logged(fn):
    def wrapper(*args, **kwargs):
        func = fn(*args, **kwargs)
        result = f"you called {fn.__name__}{args}\nit returned {func}"
        return result
    return wrapper


# @logged
# def sum_func(a, b):
#     return a + b
#
#
# print(sum_func(1, 4))
