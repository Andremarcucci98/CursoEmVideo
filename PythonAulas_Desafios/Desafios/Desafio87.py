matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = coluna = maior = 0
for j in range(0,3):
    for k in range(0,3):
        matriz[j][k]= (int(input(f'Digite um número para [{j},{k}]: ')))
print('='*30)
for j in range(0,3):
    for k in range(0,3):
        print(f'[{matriz[j][k]:^5}]',end='')
    print()
print('='*30)
for j in range(0,3):
    for k in range(0,3):
        if matriz[j][k] % 2 == 0:
            soma += matriz[j][k]
        if k == 2:
            coluna += matriz[j][k]
        if j == 1:
            if k == 0:
                maior = matriz[j][k]
            else:
                if matriz[j][k] > maior:
                    maior = matriz[j][k]
print(f'A soma dos números pares é {soma}')
print(f'A soma dos valores na terceira coluna deu {coluna}')
print(f'O maior valor da segunda linha foi {maior}')