lista = list()
pessoa = dict()
total = 0
while True:
    pessoa['Nome'] = str(input('Nome: ')).strip()
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERROR! Digite M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    lista.append(pessoa.copy())
    total += pessoa['Idade']
    choice = ' '
    if choice not in 'SsNn': choice = str(input('Cadastrar outra pessoa[S/N]?')).strip().upper()[0]
    if choice == 'N': break
print(lista)
print('=-'*20)
print(f'A) Total de pessoas cadastradas: {len(lista)}')
print(f'B) A média de idade: {total/len(lista):5.2f} anos')
print(f'C) Lista de mulheres: ',end='')
for i in lista:
    if i['Sexo'] == 'F': print(f'{i["Nome"]} ',end=', ')
print()
print(f'D) Lista de pessoas com idade superior à média: ', end=', ')
for p in lista:
    if p['Idade'] >= (total/len(lista)):
        print('   ')
        for k,v in p.items():
            print(f'{k} = {v};',end=' ')
        print()
print('<<<< PROCESSO ENCERRADO >>>>')