class Math:
    def __init__(self, first_number, second_number):
        try:
            self.first_number = int(first_number)
            self.second_number = int(second_number)
        except ValueError:
            print('Wrong arguments: please enter the number')

    @property
    def addition(self):
        return self.first_number + self.second_number

    @property
    def subtraction(self):
        return self.first_number-self.second_number

    @property
    def multiplication(self):
        return self.first_number * self.second_number

    @property
    def division(self):
        try:
            return self.first_number / self.second_number
        except ZeroDivisionError:
            return 'Division by zero!'
