import math as m

class Ovni():
    test_cases = []
    test_results = []

    def __init__(self, list: list):
        self.test_cases = list
        self.convert()
        self.calculate_area()
        self.check_if_fits()

    def convert(self):
        count = 0

        for string in self.test_cases:
            number = ""
            r1 = 0
            r2 = 0
            p = 0

            for num in string:
                if num.isdigit():
                    number += num
                elif num.isspace():
                    if r1 == 0:
                        r1 = int(number)
                        number = ""
                    elif r2 == 0:
                        r2 = int(number)
                        number = ""
            
            if p == 0:
                p = int(number)
                self.test_cases[count] = [r1, r2, p]
                count += 1

    def calculate_area(self):
        count = 0

        for ovnis in self.test_cases:
            index = 0
            for num in ovnis:
                self.test_cases[count][index] = m.pi * (ovnis[index] * ovnis[index])
                index += 1
            
            count += 1

    def check_if_fits(self):
        index = 0
        for fit in self.test_cases:
            ovnis: float = self.test_cases[index][0] + self.test_cases[index][1] 
            platform: float = self.test_cases[index][2]
            if platform - ovnis >= 0.0:
                self.test_results.append("CABE!")
                index += 1
            else:
                self.test_results.append("NÃO CABE!")
                index += 1

    def show_results(self):
        lenght = 1
        for result in self.test_results:
            if lenght != len(self.test_results):
                print(result)
                lenght += 1
            else:
            # result == len(self.test_results):
                print(result, end='')

test_cases = []

runs = int(input())

for i in range(runs):
    test = input()
    test.strip()
    test_cases.append(test)

aliens = Ovni(test_cases)
aliens.show_results()