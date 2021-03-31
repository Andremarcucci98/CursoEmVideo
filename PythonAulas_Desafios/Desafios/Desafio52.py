print('{:=^40}',' Desafio 51 ', '{:=^40}')
n = int(input('Digite um número: '))
tot = 0
for c in range(1, n+1):
    if n % c ==0:
        print('\033[33m{}'.format(c), end=' ')
        tot += 1
    else:
        print('\033[31m{}'.format(c), end=' ')
print('\nO numero {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('O numero digitado é primo')
else:
    print('O numero digitado não é primo')
