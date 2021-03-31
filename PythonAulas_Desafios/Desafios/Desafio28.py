from random import randint
from time import sleep
from termcolor import colored
print('Vamos fazer um joguinho, vou selecionar um número entre 0 e 5 e você deve adivinhá-lo...')
n1 = randint(0, 10)
n = int(input('Digite um número entre 0 e 10: '))
print(colored('PROCESSANDO','yellow'), end='', flush=True)
sleep(0.3)
print(colored('.','red'), end='', flush=True)
sleep(0.3)
print(colored('.','green'), end='', flush=True)
sleep(0.3)
print(colored('.','blue'), end='', flush=True)
sleep(0.3)
print(colored('\nPROCESSANDO','yellow'), end='', flush=True)
sleep(0.3)
print(colored('.','red'), end='', flush=True)
sleep(0.3)
print(colored('.','green'), end='', flush=True)
sleep(0.3)
print(colored('.','blue'), end='', flush=True)
sleep(0.3)
if n1 == n:
        print('Você digitou {} e o computador {}'.format(n, n1))
        print('PARABÉNS! Você acertou!!')

else:
    t = 1
    while n != n1:
        n = int(input('\nTRY AGAIN: '))
        print(colored('PROCESSANDO', 'yellow'), end='', flush=True)
        sleep(0.3)
        print(colored('.', 'red'), end='', flush=True)
        sleep(0.3)
        print(colored('.', 'green'), end='', flush=True)
        sleep(0.3)
        print(colored('.', 'blue'), end='', flush=True)
        sleep(0.3)
        t = t + 1
    print('Você acertou na {}° tentativa'.format(t))


