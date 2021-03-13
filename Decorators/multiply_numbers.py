def multiply(times):
    def decorator(function):
        def wrapper(*args, **kwargs):
            func = function(*args, **kwargs)
            return func * times
        return wrapper
    return decorator


# @multiply(5)
# def add_ten(number):
#     return number + 10
#
# print(add_ten(6))