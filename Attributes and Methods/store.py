class Store:
    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def from_size(cls, name: str, type: str, size: int):
        new_instance = cls(name, type, size//2)
        return new_instance

    def remove_item(self, item_name: str, amount: int):
        if item_name in self.items:
            if self.items[item_name] >= amount:
                self.items[item_name] -= amount
                self.capacity += amount
                return f"{amount} {item_name} removed from the store"
            return f"Cannot remove {amount} {item_name}"
        return f"Cannot remove {amount} {item_name}"

    def add_item(self, item_name: str):
        if item_name in self.items and self.capacity > 0:
            self.items[item_name] += 1
            self.capacity -= 1
            return f"{item_name} added to the store"
        elif self.capacity > 0:
            self.items[item_name] = 1
            self.capacity -= 1
            return f"{item_name} added to the store"
        return"Not enough capacity in the store"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


# first_store = Store("First store", "Fruit and Veg", 20)
# second_store = Store.from_size("Second store", "Clothes", 500)
#
# print(first_store)
# print(second_store)
#
# print(first_store.add_item("potato"))
# print(second_store.add_item("jeans"))
# print(first_store.remove_item("tomatoes", 1))
# print(second_store.remove_item("jeans", 1))
