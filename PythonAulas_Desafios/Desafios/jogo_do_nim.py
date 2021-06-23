"""
------------------- JOGO DO NIM ------------------------
"""


def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        remove2 = n % (m+1)
        if remove2 > 0:
            return remove2
    return m


def usuario_escolhe_jogada(n, m):
    remove1 = 0
    while remove1 == 0:
        remove1 = int(input('\nQuantas peças você vai tirar? '))
        if remove1 > n or remove1 < 1 or remove1 > m:
            print('\nOops! Jogada inválida! Tente de novo.\n')
            remove1 = 0
    return remove1


def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    computer_turn = True

    if n % (m + 1) == 0:
        computer_turn = False
        print('\nVocê começa!')
    else:
        print('\nComputador começa!')
    while n > 0:
        if computer_turn:
            turno = computador_escolhe_jogada(n, m)
            computer_turn = False
            if turno == 1:
                print('\nO computador tirou uma peça.')
            else:
                print(f'\nO computador tirou {turno} peças')
        else:
            turno = usuario_escolhe_jogada(n, m)
            computer_turn = True
            if turno == 1:
                print('\nVocê tirou uma peça.')
            else:
                print(f'\nVocê tirou {turno} peças')
        n = n - turno
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
        elif n > 1:
            print(f'Agora restam {n} peças no tabuleiro.')
    if computer_turn:
        print('Fim de jogo! Você ganhou!')
        return 1
    else:
        print('Fim de jogo! O computador ganhou!')
        return 0


def campeonato():
    usuario = computador = 0
    for x in range(1, 4):
        print(f'\n**** Rodada {x} ****\n')
        vencedor = partida()
        if vencedor == 1:
            usuario = usuario + 1
        else:
            computador = computador + 1
    print('\n**** Final do campeonato! ****\n')
    print(f'Placar: Você {usuario} x {computador} Computador')


tipo = 0
while tipo == 0:
    tipo = int(input('Bem-vindo ao jogo do NIM! Escolha:\n'
                     '\n1 - Para jogar uma partida'
                     '\n2 - Para jogar um campeonato '))
    if tipo == 1:
        print('\nVocê escolheu partida isolada!')
        partida()
        break
    elif tipo == 2:
        print('\nVocê escolheu um campeonato!')
        campeonato()
        break
    else:
        print('Opção inválida!')
        tipo = 0
