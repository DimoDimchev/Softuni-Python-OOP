import random


class RandomList(list):
    def get_random_element(self):
        random_element = random.choice(self)
        self.pop(self.index(random_element))
        return random_element
