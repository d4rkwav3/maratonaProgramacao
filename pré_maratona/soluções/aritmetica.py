class Calc():
    elements: str = []
    element_0_num = None
    element_1_op = None
    element_2_num = None
    element_3_op = None
    element_4_num = None
    zero_division_error = False
    result = None

    def __init__(self, expression: list):
        self.elements = expression
        self.zero_division_error = False
        self.remove_ws()
        self.convert()
        self.calculate()

    def remove_ws(self):
        for each in range(len(self.elements)):
            self.elements[each].strip()

    def convert(self):
        self.element_0_num = None
        self.element_1_op = None
        self.element_2_num = None
        self.element_3_op = None
        self.element_4_num = None

        for each in self.elements:
            if each.isdigit():
                if self.element_0_num == None:
                    self.element_0_num = int(each)
                elif self.element_2_num == None:
                    self.element_2_num = int(each)
                elif self.element_4_num == None:
                    self.element_4_num = int(each)
            
            elif len(each) > 1:
                if each[1].isdigit():
                    if self.element_0_num == None:
                        self.element_0_num = int(each)
                    elif self.element_2_num == None:
                        self.element_2_num = int(each)
                    elif self.element_4_num == None:
                        self.element_4_num = int(each)

            else:
                if self.element_1_op == None:
                    self.element_1_op = each
                elif self.element_3_op == None:
                    self.element_3_op = each

    def plus(self, numA: int, numB: int):
        # if self.result != None:
        #     if self.element_1_op == "*" or self.element_1_op == "/":
        #         return numA + self.result
        #     else:
        #         return self.result + numA
        # else:
        return numA + numB

    def minus(self, numA: int, numB: int):
        # if self.result != None:
        #     if self.element_1_op == "*" or self.element_1_op == "/":
        #         return numA - self.result
        #     else:
        #         return self.result - numA
        # else:
        return numA - numB

    def times(self, numA: int, numB: int):
        # if self.result != None:
        #     if self.element_1_op == "*" or self.element_1_op == "/":
        #         return numA * self.result
        #     else:
        #         return self.result * numA
        # else:
        return numA * numB

    def divided(self, numA: int, numB: int):
        if numB == 0:
            self.zero_division_error = True
        # elif self.result != None:
        #     if self.element_1_op == "*" or self.element_1_op == "/":
        #         if self.result == 0:
        #             self.zero_division_error = True
        #         else:
        #             return numA // self.result
        #     else:
        #         if numA == 0:
        #             self.zero_division_error = True
        #         else:
        #             return self.result // numA
        else:
            return numA // numB

    def calculate(self):
        self.result = None

        if self.element_1_op == "*" and self.zero_division_error == False:
            self.result = self.plus(self.element_0_num, self.element_2_num)
            if self.element_3_op == "*":
                self.result = self.times(self.result, self.element_4_num)
            elif self.element_3_op == "/":
                self.result = self.divided(self.result, self.element_4_num)
            # elif self.element_3_op == "/" and self.element_4_num == 0:
            #     self.zero_division_error = True
            #     # self.result = "erro"
            elif self.element_3_op == "+":
                self.result = self.plus(self.result, self.element_4_num)
            elif self.element_3_op == "-":
                self.result = self.minus(self.result, self.element_4_num)

        elif self.element_1_op == "/" and self.zero_division_error == False:
            self.result = self.divided(self.element_0_num, self.element_2_num)
            if self.element_3_op == "*" and self.zero_division_error == False:
                self.result = self.times(self.result, self.element_4_num)
            elif self.element_3_op == "/" and self.zero_division_error == False:
                self.result = self.divided(self.result, self.element_4_num)
            # elif self.element_3_op == "/" and self.element_4_num == 0 and self.zero_division_error == False:
            #     self.zero_division_error = True
            #     # self.result = "erro"
            elif self.element_3_op == "+":
                self.result = self.plus(self.result, self.element_4_num)
            elif self.element_3_op == "-":
                self.result = self.minus(self.result, self.element_4_num)
        
        # elif self.element_1_op == "/" and (self.element_0_num == 0 or self.element_2_num == 0) and self.zero_division_error == False:
        #     self.zero_division_error = True
        #     self.result = "erro"

        elif self.element_3_op == "*" and self.zero_division_error == False:
            self.result = self.times(self.element_2_num, self.element_4_num)
            # if self.element_1_op == "*":
            #     self.result = self.plus(self.element_0_num, self.result)
            # elif self.element_1_op == "/":
            #     self.result = self.divided(self.element_0_num, self.result)
            # elif self.element_1_op == "/" and self.result == 0:
            #     self.zero_division_error = True
            if self.element_1_op == "+":
                self.result = self.plus(self.element_0_num, self.result)
            elif self.element_1_op == "-":
                self.result = self.minus(self.element_0_num, self.result)

        elif self.element_3_op == "/" and self.zero_division_error == False:
            self.result = self.divided(self.element_2_num, self.element_4_num)
            # if self.element_3_op == "/" and self.element_4_num == 0:
            #     self.zero_division_error = True
            if self.element_1_op == "+":
                self.result = self.plus(self.element_0_num, self.result)
            elif self.element_1_op == "-":
                self.result = self.minus(self.element_0_num, self.result)

        # elif self.element_3_op == "/" and (self.element_2_num == 0 or self.element_4_num == 0) and self.zero_division_error == False:
        #     self.zero_division_error = True
        #     self.result = "erro"

    def show_result(self):
        if self.zero_division_error:
            print('erro', end='')
        else:
            print(self.result, end='')

input_list = []
for i in range(5):
    input_list.append(input())

calculadora = Calc(input_list)
calculadora.show_result()