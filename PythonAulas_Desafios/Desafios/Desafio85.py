numeros = [[], []]
valor = 0
for p in range(1,8):
    valor = int(input(f'Digite o {p}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('=-='*20)
numeros[0].sort()
numeros[1].sort()
print(f'Valores pares: {numeros[0]}')
print(f'Valores ímpares: {numeros[1]}')
