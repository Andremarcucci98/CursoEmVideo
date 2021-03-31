print('=-='*5, 'Desafio 42', '=-='*5)
n1 = float(input('Digite o valor do lado 1: '))
n2 = float(input('Digite o valor do lado 2: '))
n3 = float(input('Digite o valor do lado 3: '))
#CONDIÇÕES
if (n1 < (n2 + n3)) and (n2 < (n1 + n3)) and (n3 < (n1 + n2)):
    if n1 == n2 == n3:
        print('O triângulo é equilátero.')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('O triângulo é isósceles.')
    elif n1 != n2 != n3:
        print('O triângulo é escaleno.')
else:
    print('\033[0;31mAs medidas selecionadas não formam um triângulo.\033[m')