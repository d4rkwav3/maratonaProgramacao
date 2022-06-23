class Potencia:
    __a = 0
    __b = 0

    def set_a(self, number):
        self.__a = number

    def set_b(self, number):
        self.__b = number

    def get_result(self):
        result = self.__a ** self.__b
        return result

n = Potencia()

n.set_a(int(input("")))
n.set_b(int(input("")))

print(n.get_result(), end="")