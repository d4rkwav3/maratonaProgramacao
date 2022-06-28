entrada = []
resultado = []
n_entradas = int(input())

for string in range(n_entradas):
    enter = input()
    entrada.append(enter)

abre = num_abre = 0
fecha = num_fecha = 0
par_abre_fecha = 0

for string in entrada:
    for char in string:
        if char == '(':
            abre += 1 
            num_abre += 1
        elif char == ')':
            num_fecha += 1
            fecha += 1
            if abre > fecha or abre == fecha:
                par_abre_fecha += 1
                fecha -= 1
                abre -= 1

    if (num_abre + num_fecha) // 2 == par_abre_fecha:
        resultado.append("OK")
    else:
        resultado.append("NOK")
    
    abre = num_abre = fecha = num_fecha = par_abre_fecha = 0

for index in range(len(resultado)):
    if index < len(resultado) - 1:
        print(resultado[index])
    elif index == len(resultado) - 1:
        print(resultado[index], end='')