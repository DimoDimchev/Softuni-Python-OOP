def make_bold(fn):
    def wrapper(*args):
        func = fn(*args)
        result = f"<b>{func}</b>"
        return result
    return wrapper


def make_italic(fn):
    def wrapper(*args):
        func = fn(*args)
        result = f"<i>{func}</i>"
        return result
    return wrapper


def make_underline(fn):
    def wrapper(*args):
        func = fn(*args)
        result = f"<u>{func}</u>"
        return result
    return wrapper


# @make_bold
# @make_italic
# @make_underline
# def greet(name):
#     return f"Hello, {name}"
#
#
# print(greet("Peter"))
