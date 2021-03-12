class dictionary_iter:
    def __init__(self, dict):
        self.dict = dict
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        unpacked = [(key, value) for key, value in self.dict.items()]
        while self.index <= (len(unpacked) - 1):
            element = unpacked[self.index]
            self.index += 1
            return element
        raise StopIteration


# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)