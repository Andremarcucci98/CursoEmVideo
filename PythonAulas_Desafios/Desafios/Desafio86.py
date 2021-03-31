matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for j in range(0,3):
    for k in range(0,3):
        matriz[j][k]= (int(input(f'Digite um número para [{j},{k}]: ')))
print('='*30)
for j in range(0,3):
    for k in range(0,3):
        print(f'[{matriz[j][k]:^5}]',end='')
    print()