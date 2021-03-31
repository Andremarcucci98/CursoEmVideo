print('{:=^40}'.format(' CADASTRAMENTO DE PESSOAS '))
contfem = contmasc = maioridade = f_menor20 = 0
while True:
    sexo = choice = ' '
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        contmasc += 1
    elif sexo == 'F':
        contfem += 1
        if idade < 20:
            f_menor20 += 1
    print('{:.^40}'.format('.'))
    while choice not in 'YN':
            choice = str(input('Gostaria de cadastrar outra pessoa [Y/N]? ')).strip().upper()[0]
    print('{:.^40}'.format('.'))
    if choice == 'N':
        break
print('Pessoas com idade superior a 18 anos: {}'
      '\nHomens cadastrados: {}'
      '\nMulheres menores de 20 anos: {}'.format(maioridade, contmasc, contfem))
print('{:.^40}'.format('.'))
