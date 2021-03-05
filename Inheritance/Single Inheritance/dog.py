from project.animal import Animal

class Dog(Animal):
    def bark(self):
        return "barking..."

sirma = Dog()
print(sirma.eat)
print(sirma.bark)