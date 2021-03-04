class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = {}

    def get_name(self):
        return self.__name

    def get_dough(self):
        return self.__dough

    @property
    def toppings(self):
        return self.__toppings

    def get_toppings_capacity(self):
        return self.__toppings_capacity

    def set_name(self, new_value):
        self.__name = new_value

    def set_dough(self, new_value):
        self.__dough = new_value

    @toppings.setter
    def toppings(self, new_value):
        self.__toppings = new_value

    def set_toppings_capacity(self, new_value):
        self.__toppings_capacity = new_value

    def add_topping(self, topping):
        toppings = sum(self.__toppings.values())
        if toppings < self.__toppings_capacity:
            if topping.get_topping_type() not in self.__toppings:
                self.__toppings[topping.get_topping_type()] = 0
            self.__toppings[topping.get_topping_type()] += topping.get_weight()
        else:
            raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self):
        total_weight = sum(self.__toppings.values())
        return total_weight

