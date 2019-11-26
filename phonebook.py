class PhoneBook:

    def __init__(self):
        self.numbers = {}

    def add(self, name, number):
        self.numbers[name] = number
        pass

    def lookup(self, name):
        return self.numbers[name]
        pass

    def is_consistent(self):
        for name1, number1 in self.numbers.items():
            for name2, number2 in self.numbers.items():
                if name1 is name2:
                    continue
                if number1.startswith(number2):
                    return False
        return True