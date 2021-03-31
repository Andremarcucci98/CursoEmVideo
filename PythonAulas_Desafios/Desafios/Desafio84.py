dados = list()
pessoas = list()
maispesados = mleve = 0
cont = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maispesados = mleve = dados[1]
    else:
        if dados[1] > maispesados:
            maispesados = dados[1]
        if dados[1] < mleve:
            mleve = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    cont += 1
    choice =' '
    while choice not in 'SsNn':
        choice = str(input('Gostaria de cadastrar outra pessoa [S/N]?')).upper().strip()[0]
    if choice == 'N':
        break
print(f'{cont} pessoas foram cadastradas')
print(f'O maior peso foi de {maispesados}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maispesados:
        print(f'{p[0]}', end='')
print(f'O menor peso foi de {mleve}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == mleve:
        print(f'{p[0]}', end='')