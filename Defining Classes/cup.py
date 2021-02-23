class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, amount):
        if self.size - (self.quantity + amount) >= 0:
            self.quantity += amount

    def status(self):
        return self.size - self.quantity


# UNCOMMENT FOR TESTING PURPOSES
# cup = Cup(100, 50)
# cup.fill(50)
# cup.fill(10)
# print(cup.status())