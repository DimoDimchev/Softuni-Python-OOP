def fibonacci():
    prev_number = 0
    current_number = 1
    while True:
        yield prev_number
        prev_number, current_number = current_number, prev_number + current_number


# generator = fibonacci()
# for i in range(5):
#     print(next(generator))