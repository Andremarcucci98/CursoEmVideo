print('-=-'*5,'Desafio 37','-=-'*5)
from time import sleep
n = int(input('Digite um número inteiro: '))
lista = str(input('Para convesão em \033[0;31m binário\033[m digite [1]'
                  '\npara conversão em \033[0;31m octal\033[m digite [2] '
                  '\npara conversão em \033[0;31m hexadecimal\033[m digite [3]:  ')).strip()
n1 = n
if lista[:1] == '1':
    print('Você escolheu conversão em binário.',end='',flush=True)
    sleep(0.5)
    cont = ''
    while n / 2 > 0:
        cont = cont + str(n % 2)
        n = n // 2
    bin = cont[::-1]
    print('\nO número \033[0;31m{}\033[m em binário será \033[0;31m{}\033[m'.format(n1, bin))

elif lista[:1] == '2':
    print('Você escolheu conversão em octal.',end='',flush=True)
    sleep(0.5)
    cont = ''
    while n / 8 > 0:
        cont = cont + str(n % 8)
        n = n //8
    octal = cont[::-1]
    print('O numero \033[0;31m {}\033[m em octal será \033[0;31m{}\033[m.'.format(n1, octal))

elif lista[:1] == '3':
    print('Você escolheu conversão em hexadecimal.',end='',flush=True)
    sleep(0.5)
    hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    cont = ''
    while n / 16 > 0:
        cont = cont + str(hex[(n % 16)])
        n = n // 16
    hexadec = cont[::-1]
    print('O numero \033[0;31m{}\033[m em hexadecimal será \033[0;31m{}\033[m.'.format(n1, hexadec))
else:
    print('Você \033[0;31m não\033[m selecionou nenhuma das opções')
