import math


class AverageCalculating:
    def __init__(self):
        self.numbers = []
        self.result = self.calculate_average()

    def calculate_average(self):
        if self.numbers:
            self.result = math.floor(sum(self.numbers) / len(self.numbers))
            return self.result
        return None

    def show_result(self):
        if not self.result:
            print("Был введён пустой список.")
        else:
            print(f"Среднее арифметическое списка {self.numbers}: {self.result}."
                  f"\nОтвет округляется в меньшую степень до целого.")
