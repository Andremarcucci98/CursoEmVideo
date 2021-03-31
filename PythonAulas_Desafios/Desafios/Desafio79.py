lista = []
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado...')
    else:
        print('Este número já está na lista, portanto não será acrescentado.')
    choice = ' '
    choice = str(input('Quer adicionar outro elemento [S/N]? ')).upper().strip()[0]
    while choice not in 'SN':
        choice = str(input('Quer adicionar outro elemento [S/N]? ')).upper().strip()[0]
    if choice == 'N':
        break
lista.sort()
print(lista)

