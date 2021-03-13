def type_check(type_of_arg):
    def decorator(fn):
        def wrapper(arg):
            if type(arg) != type_of_arg:
                return "Bad Type"
            else:
                func = fn(arg)
                return func
        return wrapper
    return decorator


# @type_check(int)
# def times2(num):
#     return num*2
#
#
# print(times2(2))
# print(times2('Not A Number'))
