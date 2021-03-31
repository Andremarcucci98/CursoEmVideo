print('-=-'*5,'Comparando numeros','-=-'*5)
n1 = int(input('Digite um primeiro numero: '))
n2 = int(input('Digite o segundo: '))
n3 = int(input('Digite o terceiro: '))
lista = [n1,n2,n3]
if n1 > n2 and n1 > n3:
    print('{} é o maior'.format(n1))
    if n2 > n3:
        print('{} é o menor'.format(n3))
    else:
        print('{} é o menor'.format(n2))
elif n2 > n1 and n2 > n3:
    print('{} é o maior'.format(n2))
    if n1 > n3:
        print('{} é o menor'.format(n3))
    else:
        print('{} é o menor'.format(n1))
elif n3 > n1 and n3 > n2:
    print('{} é o maior'.format(n3))
    if n1 > n2:
        print('{} é o menor'.format(n2))
    else:
        print('{} é o menor'.format(n1))
