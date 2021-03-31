print('======== Desafio 23 ========')
import math
n = int(input('Digite um número entre 0 e 9999: '))
print('O numero ddigitado foi {}'.format(n))
unidade = math.floor(n%10)
print('Unidade: ',unidade)
dezena = math.floor((n//10)%10)
print('Dezena: ', dezena)
centena = math.floor((n//100)%10)
print('Centena: ',centena)
milhar = math.floor((n//1000)%10)
print('Milhar: ', milhar)

