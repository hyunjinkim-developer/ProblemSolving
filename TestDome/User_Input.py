"""
Problem: https://www.testdome.com/questions/python/user-input/110603
"""

class TextInput:
    def __init__(self):
        self.value = ""

    def add(self, character):
        self.value += character

    def get_value(self):
        return self.value


# Inherits class TextInput
class NumericInput(TextInput):
    def add(self, character):
        if character.isdigit():
            self.value += character


if __name__ == '__main__':
    input = NumericInput()
    input.add("1")
    input.add("a")
    input.add("0")
    print(input.get_value())