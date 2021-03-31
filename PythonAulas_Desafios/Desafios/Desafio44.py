print('{:=^40}'.format(' Desafio 43 '))
preco = float(input('Digite o preço do produto: '))
condicao = str(input('Digite '
                     '\n[1] para pagamento à vista no dinheiro,'
                     '\n[2] para à vista no cartão,'
                     '\n[3] para 2x no cartão,'
                     '\n[4] para 3x ou mais no cartão: '))
if condicao == '1':
    precod = preco * 0.9
    print('À vista no dinheiro, o produto sairá por R${:.2f}.'.format(precod))
elif condicao == '2':
    precod = preco * 0.95
    print('À vista no cartão, o preço sairá por R${:.2f}.'.format(precod))
elif condicao == '3':
    print('2x no cartão, o preço sairá por R${:.2f}.'.format(preco))
elif condicao == '4':
    precod = preco * 1.20
    print('3x ou mais no cartão, o preço sairá por R${:.2f}.'.format(precod))
else:
    print('Nenhuma opção foi escolhida, boas compras.')