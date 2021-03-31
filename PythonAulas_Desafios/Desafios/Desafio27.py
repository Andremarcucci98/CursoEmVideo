nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
print('Seu primeiro nome é {} e seu último nome é {}'.format(lista[0], lista[len(lista)-1])) #lista[-1]))