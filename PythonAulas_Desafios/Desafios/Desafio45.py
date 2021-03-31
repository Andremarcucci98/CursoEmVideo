print('=-='*5,'Jokenpô','=-='*5)
from random import choice
from time import sleep
h = str(input('Você quer jogar jogar? ')).strip().upper()
if h == 'SIM':
    pessoa = str(input('Escolha entre pedra, papel ou tesoura: ')).strip().upper()
    computador = choice(['PEDRA','PAPEL','TESOURA'])
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!')
    print('='*50)
    while pessoa == computador:
        pessoa = str(input('Escolha novamente entre pedra, papel ou tesoura: ')).strip().upper()
        computador = choice(['PEDRA', 'PAPEL', 'TESOURA'])
    #PESSOA PERDE
    if ((pessoa == 'PEDRA' and computador == 'PAPEL')
        or (pessoa == 'PAPEL' and computador == 'TESOURA')
        or (pessoa == 'TESOURA' and computador == 'PEDRA')):
        print('Você perdeu!! Eu escolhi {} e você {}'.format(computador, pessoa))
    elif ((pessoa == 'PEDRA' and computador == 'TESOURA')
          or (pessoa == 'PAPEL' and computador == 'PEDRA')
          or (pessoa == 'TESOURA' and computador == 'PAPEL')):
        print('Parabéns, você me derrotou!! Eu escolhi {} e você {}'.format(computador,pessoa))
else:
    print('Tudo bem, quem sabe na próxima.')


