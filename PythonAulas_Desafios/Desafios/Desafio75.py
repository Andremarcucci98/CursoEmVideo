print('======== DESAFIO 75 =========')
numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite um último número: ')))
print(f'Valores digitados: {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 apareceu na posição {numeros.index(3)+1}',end='')
else:
    print('O número 3 não foi digitado em nenhuma posição')
for n in numeros:
    if n % 2 == 0:
        print(n, end =' ')