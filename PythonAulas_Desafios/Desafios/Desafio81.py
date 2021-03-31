lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    choice = ' '
    while choice not in 'SN':
        choice = str(input('Gostaria de digitar outro numero [S/N]? ')).upper().strip()[0]
    if choice == 'N':
        break
print('-'*30)
print(f'Lista digitada: {lista}')
print(f'Numero de elementos: {len(lista)}')
lista.sort(reverse=True)
print(f'Lista em ordem descrescente: {lista}')
if 5 not in lista:
    print('O número 5 não está na lista.')
else:
    print(f'O número 5 se encontra na/as posição/ões',end=' ')
    for i, v in enumerate(lista):
        if v == 5:
            print(f'{i+1}...',end='')
print('\n')
print('-'*30)
