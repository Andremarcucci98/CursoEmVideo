print('{:=^40}'.format(' DESAFIO 70 '))
print('{:.^40}'.format(' LISTA DE COMPRAS '))
total = m_barato = acimade1000 = n = 0
maisbarato = ''
while True:
    produto = str(input('Produto: ')).strip().upper()
    preco = float(input('Preço: R$ '))
    total += preco
    n += 1
    if preco > 1000.00:
        acimade1000 += 1
    if n == 1:
        m_barato = preco
        maisbarato = produto
    else:
        if preco < m_barato:
            m_barato = preco
            maisbarato = produto
    choice = ' '
    while choice not in 'YN':
        choice = str(input('Gostaria de adicionar algum item [Y/N]: ')).strip().upper()[0]
    if choice == 'N':
        break
print('{:.^40}'.format('.'))
print(f'TOTAL GASTO: R${total:.2f}'
      f'\nPRODUTOS COM PREÇO MAIOR DO QUE R$1000,00: {acimade1000}'
      f'\nPRODUTO MAIS BARATO: {maisbarato} COM VALOR R${m_barato:.2f}')