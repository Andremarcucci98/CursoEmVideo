print('===== Desafio57=====')
sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Valor incoerente, digite novamente seu sexo [M/F]: ')).strip().upper()[0]
print('O sexo digitado foi {}'.format(sexo))


