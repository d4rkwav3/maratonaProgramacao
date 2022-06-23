class Somatorio():
    numbers = []
    somas = []

    def __init__(self, list):
        self.numbers = list
        self.convert()
        self.somar()

    def convert(self):
        converted_list = []
        only_numbers = ""

        for strings in self.numbers:

            for letters in range(len(strings)):
                if strings[letters].isdigit():
                    only_numbers += strings[letters]

                elif strings[letters] == ";":
                    converted_list.append(int(only_numbers))
                    only_numbers = ""

            converted_list.append(int(only_numbers))    
            self.somas.append(converted_list)
            only_numbers = ""
            converted_list = []

    def somar(self):
        somatoria = 0

        for index in range(len(self.somas)):
            for num in self.somas[index]:
                somatoria += num

            self.somas[index] = somatoria
            somatoria = 0

    def exibir_somatoria(self):
        for somas in self.somas:
            if somas != self.somas[-1]:
                print(somas)
            elif somas == self.somas[-1]:
                print(somas, end='')

teste = []
runs = int(input())

for i in range(runs):
    num = input()
    teste.append(num)

soma = Somatorio(teste)
soma.exibir_somatoria()
