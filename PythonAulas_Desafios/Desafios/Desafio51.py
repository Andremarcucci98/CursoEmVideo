print('=-='*20, 'Desafio 51', '=-='*20)
prim = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razao da P.A.: '))
decimo = prim + (10-1) * razao
for i in range(prim, decimo + razao, razao):
    print('{}'.format(i), end= ' -> ')
print('ACABOU')
