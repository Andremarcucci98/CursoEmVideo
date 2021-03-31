print('{:=^40}'.format(' Desafio49 '))
n = int(input('Digite um número para saber sua tabuada: '))
print('====== TABUADA DO {} ======'.format(n))
for c in range(0, 11,1):
    m = n * c
    print('{}x{} = {}'.format(n, c, m))
print('====== Bons Estudos! ======')
