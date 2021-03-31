from math import hypot
ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
h = hypot (co,ca)
print(f'O valor da hipotenusa é {h :.2f}')