class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.num < (self.count + 1):
            curr_element = self.count - self.num
            self.num += 1
            return curr_element
        raise StopIteration


# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")