class ArithmeticClass:

    def __init__(self, number_one, number_two):
        self.number_one = number_one
        self.number_two = number_two

    def add(self):
        result = self.number_one + self.number_two
        return result

    def mul(self):
        result = self.number_one * self.number_two
        return result

    def sub(self):
        result = self.number_one - self.number_two
        return result

    def div(self):
        result = self.number_one / self.number_two
        return result