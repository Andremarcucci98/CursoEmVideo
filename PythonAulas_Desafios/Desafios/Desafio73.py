print('======= BRASILEIRÃO 2019 =======')
tabela = ['Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians',
          'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará SC', 'Cruzeiro',
          'CSA', 'Chapecoense', 'Avaí']
print('{:=^40}'.format(' 5 Primeiros Colocados '))
for pos, time in enumerate(tabela[:4]):
    print(f'{pos+1}° - {time}')
print('{:=^40}'.format(''))
print('{:=^40}'.format(' 4 Últimos Colocados '))
for pos, time in enumerate(tabela[15:]):
    print(f'{pos+16}º - {time}')
print('{:=^40}'.format(''))
print('{:=^40}'.format(' Ordem Alfabética '))
tabela1 = sorted(tabela)
for n in range(0, len(tabela)):
    print(tabela1[n])
print('{:=^40}'.format(''))
print('{:=^40}'.format(' Posição da Chape '))
print(f'A Chape está na {tabela.index("Chapecoense")+1}º posição')
print('{:=^40}'.format(''))
while True:
    choice = str(input('Gostaria de consultar a posição de outro time [S/N]? ')).strip().upper()[0]
    if choice == 'N':
        break
    else:
        time = str(input('Digite o time corretamente: ')).capitalize().strip()
        print(f'{time} está na {tabela.index(time)+1}º posição')
print('========= FUTEBOL 2019 É UM PATROCÍNIO BRAHMA ===============')