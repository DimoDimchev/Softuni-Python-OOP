class vowels:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index <= (len(self.data) - 1):
            letter = self.data[self.index]
            self.index += 1
            if self.is_vowel(letter):
                return letter

        raise StopIteration

    @staticmethod
    def is_vowel(letter):
        vowel_list = ["a", "e", "i", "o", "u", "y"]
        return letter.lower() in vowel_list



# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)