print('===== Desafio 60 =====')
n = int(input('Digite um número para saber seu fatorial: '))
cont = 0
f = 1
print('Calculando {}!'.format(n))
for cont in range(1, n):
    f *= n
    n -= 1
print('fatorial: {}'.format(f))
 #   print('{}'.format(cont), end= '')
  #  print(' x ' if cont > 1 else ' = ', end='')
  #  f *= cont
  #  cont -= 1
#print('{}'.format(f))