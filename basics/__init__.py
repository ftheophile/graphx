def adder(arg):
    total = 0
    for val in arg:
        total += val
    return total


class MyClass:

    def __init__(self):
        self.numbers = []
        pass

    def __del__(self):
        del self.numbers

    def add_number(self, new_number):
        self.numbers += [new_number]

    def get_numbers(self):
        return self.numbers
