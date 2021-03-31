n1 = int(input('Digite o valor de um comprimento de reta: '))
n2 = int(input('Digite o valor de outro comprimento de reta: '))
n3 = int(input('Digite o valor de mais um comprimento de reta: '))
if (n2 - n3) < n1 < (n2 + n3) and (n1 - n3) < n2 < (n1 + n3) and (n1 - n2) < n3 < (n1 + n2):
    print('Os segmentos de reta formam um triângulo')
else:
    print('Os segmentos de reta Não formam um triângulo')