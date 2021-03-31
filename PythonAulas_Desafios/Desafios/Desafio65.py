print('====== DESAFIO 65 ======')
choice = 'Y'
n = cont = soma = menor = maior = 0
while choice == 'Y':
    n = int(input('Digite um numero:'))
    choice = str(input('Gostaria de digitar outro numero [Y/N]? ')).strip().upper()[0]
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('O maior valor é {} , o menor é {} e a media é {}'.format(maior, menor, soma/cont))