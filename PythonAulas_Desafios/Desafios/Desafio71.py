print('{:=^40}'.format(' BANCO ITAÚ '))
n = int(input('Digite um valor para sacar: R$'))
total = n
céd = 50
totced = 0
while True:
    if total >= céd:
        total -= céd
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 1
        totced = 0
        if total == 0:
            break
print('='*40)
