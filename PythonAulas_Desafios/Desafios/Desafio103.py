def jogador(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')


print('=-'*20)
nome = str(input('Digite o nome do jogador: ')).strip()
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if nome == '':
    jogador(gol=g)
else:
    jogador(nome, g)




