from random import randint
from time import sleep
numeros = list()


def sorteia(lst):
    for i in range(0,5):
        numeros.append(randint(0,15))
    print(f'Números sorteados: {numeros}')


def somapar(lst):
    soma = 0
    for k in numeros:
        if (k % 2) == 0:
            soma += k
    print(f'Soma dos números pares: {soma}')

sorteia(numeros)
somapar(numeros)