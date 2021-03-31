print('-=-'*5,'Desafio 31', '-=-'*5)
km = float(input('Digite a distância de sua viagem: '))
if km <= 200.0:
    print('Sua distância é de {:.2f}'.format(km))
    preco = km*0.5
    print('\nO preço a ser cobrado será de R${:.2f}'.format(preco))
else:
    print('Sua distância é de {:.2f}'.format(km))
    preco = km * 0.45
    print('\nO preço a ser cobrado será de R${:.2f}'.format(preco))