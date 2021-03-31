lista = []
maior = 0
menor = 0
for k in range(0,5):
    lista.append(int(input('Atribua um valor para {}ª posição: '.format(k+1))))
    if k == 0:
        maior = menor = lista[k]
    else:
        if lista[k] > maior:
            maior = lista[k]
        if lista[k] < menor:
            menor = lista[k]
print(f'Lista criada: {lista}')
print(f'O maior valor é {maior} e está na posição ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...',end='')
print(f'\nO menor valor é {menor} e está na posição ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...',end='')