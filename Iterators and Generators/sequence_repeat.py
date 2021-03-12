class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0
        self.moves = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.moves != self.number:
            if self.index < len(self.sequence):
                move = self.sequence[self.index]
                self.index += 1
                self.moves += 1
                return move
            else:
                self.index = 0
                move = self.sequence[self.index]
                self.index += 1
                self.moves += 1
                return move
        raise StopIteration()


# result = sequence_repeat('dimo', 5)
# for item in result:
#     print(item, end ='')