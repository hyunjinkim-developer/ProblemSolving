"""
Problem:
https://www.testdome.com/questions/python/ice-cream-machine/94857
"""

class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        combinations = list()
        for ingredient in self.ingredients:
            for topping in self.toppings:
                combinations.append([ingredient, topping])
        return combinations


if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops())  # should print: [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]