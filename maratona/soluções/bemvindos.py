participantes = []
num_parti = int(input())

for member in range(num_parti):
    participante = input()
    participantes.append(participante)

participantes.sort()

for member in range(len(participantes)):
    if member < len(participantes) - 1:
        print(f"Bem-vindo(a), {participantes[member]}!!!")
    elif member == len(participantes) - 1:
        print(f"Bem-vindo(a), {participantes[member]}!!!", end='')