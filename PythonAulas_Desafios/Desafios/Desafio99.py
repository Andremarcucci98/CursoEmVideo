from time import sleep


def maior(*num):
    maior = contador = 0
    print('Analisando valores', end='')
    print('.', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print()
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'Foram informados {contador} valores ao todo')
    print(f'O maior valor informado foi {maior}')
    print('-='*15)


maior(8, 6, 9, 4, 5)
maior(8, 6, 9)
maior(8, 6)
maior(8)
maior()