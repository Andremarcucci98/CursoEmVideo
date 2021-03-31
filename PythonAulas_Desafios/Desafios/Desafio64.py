print('====== Desafio 64 ======')
cont = 0
soma = 0
n = int(input('Digite um numero: '))
while n != 999:
    cont += 1
    soma = soma + n
    n = int(input('Digite outro: '))
print('\n{} numero foram digitados'
      ', cuja soma é {}'.format(cont,soma))
