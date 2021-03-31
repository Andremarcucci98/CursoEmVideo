print('{:=^40}'.format('Desafio50'))
from random import randint
s = 0
for c in range(1,7):
    n = int(input('Digite um número: '))
    if (n % 2) == 0:
        s += c
print('A soma dos valores pares digitados possui valor {}'.format(s))


