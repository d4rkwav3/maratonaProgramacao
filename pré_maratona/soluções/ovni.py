import math as m

class Ovni():
    test_cases = []
    test_results = []

    def __init__(self, list: list):
        self.test_cases = list
        self.convert()
        # self.calculate_area()
        # self.calculate_diameter()
        # self.check_if_fits()

    def convert(self):
        count = 0

        for string in self.test_cases:
            number = ""
            r1 = 0
            r2 = 0
            p = 0

            for num in string:
                if num.isdigit() or num == '.':
                    number += num
                elif num.isspace():
                    if r1 == 0:
                        r1 = float(number)
                        number = ""
                    elif r2 == 0:
                        r2 = float(number)
                        number = ""
            
            if p == 0:
                p = float(number)
                self.test_cases[count] = [r1, r2, p]
                count += 1

    def calculate_diameter(self):
        count = 0

        for ovnis in self.test_cases:
            index = 0
            for num in ovnis:
                self.test_cases[count][index] = 2 * ovnis[index]
                index += 1
            
            count += 1

    def calculate_area(self):
        count = 0

        for ovnis in self.test_cases:
            index = 0
            for num in ovnis:
                self.test_cases[count][index] = m.pi * (ovnis[index] ** 2)
                index += 1
            
            count += 1

    def check_if_fits(self):
        # index = 0
        for circle in self.test_cases:
            ovni_1: float = circle[0]
            ovni_2: float = circle[1]
            platform: float = circle[2]
            if (ovni_1 + ovni_2) <= platform:
                self.test_results.append("CABE!")
                # index += 1
            else:
                self.test_results.append("NAO CABE!")
                # index += 1

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
aliens.calculate_diameter()
aliens.check_if_fits()
aliens.show_results()