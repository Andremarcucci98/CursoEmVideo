from math import cos, sin, tan, radians
n = float(input('Digite um ângulo: '))
c = cos(radians(n))
s = sin(radians(n))
t = tan(radians(n))
print(f'O ângulo digitado é {n}° \ncosseno = {c :.3f} \nseno = {s :.3f} \ntangente = {t :.3f}')