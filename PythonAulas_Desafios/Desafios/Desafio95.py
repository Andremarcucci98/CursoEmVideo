lista = list()
jogador = dict()
gols = []
total = 0
print('-'*50)
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: ')).strip()
    num = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    gols.clear()
    for i in range(1,num+1):
        gols.append(int(input(f'Quantos gols ele fez na {i}º partida: ')))
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    lista.append(jogador.copy())
    choice = ' '
    if choice not in 'SsNn': choice = str(input('Gostaria de adicionar outro jogador [S/N]? ')).upper().strip()[0]
    if choice == 'N': break
    print('-' * 40)
print('{:=^40}'.format(' TABELA DE JOGADORES '))
print('=-'*20)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-'*50)
for k, v in enumerate(lista):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*50)
while True:
    busca = int(input('Mostrar dados de qual jogador (999 para parar)? '))
    if busca == 999:
        break
    if busca >= len(lista):
        print(f'Erro!! Não existe jogador com código {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {lista[busca]["Nome"]}:')
        for i, g in enumerate(lista[busca]['Gols']):
            print(f'-> No jogo {i} fez {g} gols')
        print('-'*40)
print('<<<< ENCERRANDO >>>>-')