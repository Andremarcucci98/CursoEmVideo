'''print('{:=^30}'.format(' MEGASENA '))
from random import randint
n = int(input('Gostaria de fazer quantos jogos?: '))
numeros = []
for i in range(1,n+1):
    print(f'{i}º jogo:',end='')
    for j in range(1,7):
        numeros.append(randint(1,60))
        print(f'{numeros}',end='')
        numeros.clear()
    print()
print('{:=^30}'.format(' <BOA SORTE> '))'''

'''from random import randint
lista = list()
jogos = list()
quant = int(input('Quantos jogos vc quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f'Sorteando {quant} jogos', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')'''

from random import sample
from time import sleep
jogos = list()
n = int(input('Quantos jogos gostaria?: '))
for c in range(n):
    a = sorted(sample(range(1,61),6))
    jogos.append(a[:])
    print(f'Jogo {c+1}: {a}')
    sleep(0.5)


