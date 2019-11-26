class PhoneBook:

    def __init__(self):
        self.numbers = {}

    def add(self, name, number):
        self.numbers[name] = number
        pass

    def lookup(self, name):
        return self.numbers[name]
        pass