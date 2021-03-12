class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.num = 0
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < self.count:
            num = self.num
            self.num += self.step
            self.i += 1
            return num
        raise StopIteration


# numbers = take_skip(10, 5)
# for number in numbers:
#     print(number)