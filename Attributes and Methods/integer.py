import math


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if type(value) == float:
            return cls(math.floor(value))
        return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(value)):
            if i > 0 and rom_val[value[i]] > rom_val[value[i - 1]]:
                int_val += rom_val[value[i]] - 2 * rom_val[value[i - 1]]
            else:
                int_val += rom_val[value[i]]
        return cls(int_val)

    @classmethod
    def from_string(cls, value):
        if type(value) == str:
            return cls(int(value))
        return "wrong type"

    def add(self, integer):
        if type(integer) == Integer:
            return self.value + integer.value
        return "number should be an Integer instance"


# first_num = Integer(10)
# second_num = Integer.from_roman("IV")
#
# print(Integer.from_float("2.6"))
# print(Integer.from_string(2.6))
# print(first_num.add(second_num))
