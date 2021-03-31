print('{:-^40}'.format(' Desafio72 '))
numeros = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete',
           'dezoito', 'dezenove', 'vinte']
while True:
    while True:
        n = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= n <= 20:
            break
    print(f'Você digitou {numeros[n]}')
    choice = ' '
    choice = str(input('Quer digitar outro valor [S/N]? ')).upper().strip()[0]
    if choice == 'N':
        break