from random import sample
n1 = str(input('Digite um nome: '))
n2 = str(input('Digite em nome: '))
n3 = str(input('Digite um nome: '))
n4 = str(input('Digite um nome: '))
lista = [n1,n2,n3,n4]
ordem = sample(lista, k=2)
print('O ordem de apresentação será: ')
print(ordem)

