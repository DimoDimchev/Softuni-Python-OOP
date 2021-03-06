class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @name.setter
    def name(self, new_value):
        self.__name = new_value

    @price.setter
    def price(self, new_value):
        self.__price = new_value