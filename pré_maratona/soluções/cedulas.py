class Contador:
    troco = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
    cedulas = (100, 50, 20, 10, 5, 2, 1)
    notas = [0, 0, 0, 0, 0, 0, 0]

    def atualizar_notas(self):
        for c in range(len(self.cedulas)):
            if self.notas[c] > 0:
                novo_valor = {self.cedulas[c]: self.notas[c]}
                self.troco.update(novo_valor)
                
    def contar_notas(self, valor: int):
        restante = valor
        n = 0
        while restante != 0:
            if restante // self.cedulas[n] > 0:
                self.notas[n] = restante // self.cedulas[n]
                restante %= self.cedulas[n]
                n += 1
            elif restante // self.cedulas[n] == 0:
                n += 1
        self.atualizar_notas()

    def visualizar_troco(self):
        v100 = f"{self.troco.get(100)} nota(s) de R$ 100\n"
        v50 = f"{self.troco.get(50)} nota(s) de R$ 50\n"
        v20 = f"{self.troco.get(20)} nota(s) de R$ 20\n"
        v10 = f"{self.troco.get(10)} nota(s) de R$ 10\n"
        v5 = f"{self.troco.get(5)} nota(s) de R$ 5\n"
        v2 = f"{self.troco.get(2)} nota(s) de R$ 2\n"
        v1 = f"{self.troco.get(1)} nota(s) de R$ 1"
        print(v100 + v50 + v20 + v10 + v5 + v2 + v1, end="")

valor = Contador()
valor.contar_notas(int(input()))
valor.visualizar_troco()