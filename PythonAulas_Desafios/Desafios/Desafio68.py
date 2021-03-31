print('{:=^40}'.format(' PAR OU ÍMPAR '))
print('Vamos jogar PAR ou ÍMPAR...')
from random import randint
pessoa = ''
cont = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(1,11)
    paridade = (jogador + computador) % 2
    pessoa = str(input('Escolha entre Par ou Ímpar [P/I]: ')).strip().upper()[0]
    if paridade == 0 and pessoa == 'P':
        print('Pessoa escolheu {} e jogou {}, '
              'computador jogou {}, logo a paridade foi {},'.format(pessoa, jogador, computador, paridade ))
    elif paridade == 1 and pessoa == 'I':
        print('Pessoa escolheu {} e jogou {}, '
              'computador jogou {}, logo a paridade foi {} '.format(pessoa, jogador, computador, paridade))
    elif paridade == 0 and pessoa == 'I':
        print('Pessoa escolheu {} e jogou {}, '
              'computador jogou {}, logo a paridade foi {} '.format(pessoa, jogador, computador, paridade))
        break
    elif paridade == 1 and pessoa == 'P':
        print('Pessoa escolheu {} e jogou {}, '
              'computador jogou {}, logo a paridade foi {},'.format(pessoa, jogador, computador, paridade))
        break
    print('PARABÉNS!! Você venceu!')
    cont += 1
print('O jogo terminou, você conseguiu me vencer {} vezes'.format(cont))




