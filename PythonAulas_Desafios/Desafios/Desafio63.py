print('====== SEQUÊNCIA DE FIBONACCI ======')
n = int(input('Digite o numero para '
              '\nmostrar os n primeiros termos da Sequência de Fibonacci: '))
p_termo = 0
s_termo = 1
proximo = 0
cont = 0
while cont != n:
    if cont == 0:
        proximo = p_termo
        print('{} ->'.format(proximo),end=' ')
    elif cont == 1:
        proximo = s_termo
        print('{} ->'.format(proximo),end=' ')
    proximo = p_termo + s_termo
    p_termo = s_termo
    s_termo = proximo
    print('{} ->'.format(proximo), end=' ')
    cont += 1
print('PAUSE')


