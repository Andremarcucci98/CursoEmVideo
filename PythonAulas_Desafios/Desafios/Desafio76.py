lista = ('Bolo de chocolate', 10.50,
         'Pão Francês', 0.50,
         'Margarina', 7.50,
         'Baguette', 2.50,
         'Suco', 5.50)
print('-'*40)
print(f'{"LISTA DO MERCADO":^40}')
print('-'*40)
for pos in range(0,len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'R${lista[pos]:>2.2f}')
print('-'*40)
