class MaiorNum:
    a = b = c = 0
    lista_entrada = []
    lista_convertida = []

    def conversao(self):
        for i in range(len(self.lista_entrada)):
            self.lista_convertida.append(int(self.lista_entrada[i]))

    def entrada(self, input: str):
        string = input
        string.strip()
        self.lista_entrada = string.split()
        self.conversao()

    def verificador(self):
        self.lista_convertida.sort(reverse=True)
        return self.lista_convertida[0]

b = MaiorNum()
b.entrada(input())
print(b.verificador(), end="")