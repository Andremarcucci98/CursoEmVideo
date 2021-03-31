print('====== Desafio59 =======')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('O que vc gostaria de fazer com eles?')
p = int(input('[1] somar'
              '\n[2] multiplicar'
              '\n[3] maior'
              '\n[4] novos números'
              '\n[5] sair do programa: '))
if p == 1:
    soma = n1 + n2
    print('A soma de {} e {} tem resultado {}'.format(n1, n2, soma))
elif p == 2:
    mult = n1 * n2
    print('A multiplicação de {} e {} tem resultado {}'.format(n1, n2, mult))
elif p == 3:
    if n1 >= n2:
        print('{} é maior do que {}'.format(n1, n2))
    else:
        print('{} é maior do que {}'.format(n2, n1))
while p == 4:
    n1 = int(input('REINICIANDO... Digite um novo valor: '))
    n2 = int(input('Digite outro: '))
    print('O que vc gostaria de fazer com eles?')
    p = int(input('[1] somar'
                  '\n[2] multiplicar'
                  '\n[3] maior'
                  '\n[4] novos números'
                  '\n[5] sair do programa: '))
    if p == 1:
        soma = n1 + n2
        print('A soma de {} e {} tem resultado {}'.format(n1, n2, soma))
    elif p == 2:
        mult = n1 * n2
        print('A multiplicação de {} e {} tem resultado {}'.format(n1, n2, mult))
    elif p == 3:
        if n1 >= n2:
            print('{} é maior do que {}'.format(n1, n2))
        else:
            print('{} é maior do que {}'.format(n2, n1))
if p == 5:
    print('Obrigado por participar.')



