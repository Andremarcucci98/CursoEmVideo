print('===== LISTA DE PESSOAS =====')
mais_velho = 0
mais_velha = 0
mais_novo = 0
mais_nova = 0
nome1 = ''
nome2 = ''
nome3 = ''
nome4 = ''
media = 0
count = 0
for p in range(1,5):
    nome = str(input('Digite o nome da {}º pessoa: '.format(p))).strip().upper()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: ')).strip().upper()
    media += idade
    if sexo == 'MASCULINO':
        if p == 1:
            mais_velho = idade
            mais_novo = idade
            nome1 = nome
        else:
            if idade > mais_velho:
                mais_velho = idade
                nome1 = nome
            if idade < mais_novo:
                mais_novo = idade
                nome2 = nome
    else:
        if idade < 20:
            count += 1
            if p ==1:
                mais_velha = idade
                mais_nova = idade
                nome3 = nome
            else:
                if idade > mais_velha:
                    mais_velha = idade
                    nome3 = nome
                if idade < mais_nova:
                    mais_nova = idade
                    nome4 = nome

print('A média de idade do grupo foi de {}'.format(media/p))
print('O homem mais velho é {} com {} anos.' .format(nome1,mais_velho))
print('A mulher mais velha é {} com {} anos.'.format(nome3,mais_velha))
print('No grupo existem {} mulheres com idade menor do que 20 anos'.format(count))
