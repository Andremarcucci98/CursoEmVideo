def maximo(x, y):
    maior = 0
    if x > y:
        maior = x
    else:
        maior = y
    return maior


n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
print(maximo(n1, n2))