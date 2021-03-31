print('{:=^40}'.format(' Desafio47 '))
n = int(input('Digite um numero: '))
if (n % 2) == 0:
    print('{:=^40}'.format(' Valores pares '))
    for c in range(0, n+2 , 2):
        print(c)
else:
    print('{:=^40}'.format(' Valores ímpares '))
    for c in range (1, n+2, 2):
        print(c)
