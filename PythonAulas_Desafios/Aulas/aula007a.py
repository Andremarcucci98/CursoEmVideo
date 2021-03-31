n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
rd = n1 % n2
print('A soma vale {},a multiplicação vale {} e a divisão vale {:.3f}'.format(s, m, d), end='>>>')
print('a potência vale {},a divisão inteira vale {} e o resto da divisão vale {}'.format(p,di,rd))