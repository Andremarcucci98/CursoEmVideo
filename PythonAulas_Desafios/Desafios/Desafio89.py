sala = list()
while True:
    nome = str(input('Nome: '))
    p1 = float(input('P1: '))
    p2 = float(input('P2: '))
    media = (p1 + p2)/2
    sala.append([nome,[p1, p2], media])
    choice = ' '
    if choice not in 'SsNn':
        choice = str(input('Gostaria de adicionar outro aluno [S/N]?: ')).upper().strip()[0]
    if choice == 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)
for i, a in enumerate(sala):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*28)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(sala)-1:
        print(f'Notas de {sala[opc][0]} são {sala[opc][1]}')
