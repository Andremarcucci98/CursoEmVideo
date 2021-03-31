print('====== DESAFIO 67 ======')
cont = 1
multip = 0
while True:
    print('{:=^40}'.format(''))
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        break
    else:
        for cont in range(1,11):
            multip = n * cont
            print(f'{n} x {cont} = {multip}')

print('{:=^40}' .format(' PROCESSO ENCERRADO '))