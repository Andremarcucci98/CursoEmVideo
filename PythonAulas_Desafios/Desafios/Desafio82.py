lista = []
lista_par = []
lista_impar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    choice = ' '
    while choice not in 'SNsn':
        choice = str(input('Quer colocar outro valor na lista? ')).upper().strip()[0]
    if choice == 'N':
        break
print('-'*40)
lista.sort()
print(f'Lista original: {lista}')
for i,v in enumerate(lista):
    if v % 2 == 0:
        lista_par.append(v)
    else:
        lista_impar.append(v)
lista_par.sort()
lista_impar.sort()
print(f'Lista com pares: {lista_par}')
print(f'Lista com impares: {lista_impar}')