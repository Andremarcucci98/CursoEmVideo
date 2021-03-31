jogador = {}
gols = []
total = 0
jogador['Nome'] = str(input('Nome do Jogador: ')).strip()
num = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for i in range(1,num+1):
    gols.append(int(input(f'Quantos gols ele fez na {i}º partida: ')))
jogador['Gols'] = gols[:]
jogador['Total'] = sum(gols)
print('=-'*20)
print(jogador)
print('=-'*20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*20)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for i, v in enumerate(jogador['Gols']):
    print(f'=> Na partida {i}, fez {v} gols')
print(f'Foi um total de {jogador["Total"]} gols')
