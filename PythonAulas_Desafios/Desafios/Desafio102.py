def fatorial(numero, show):
    """
    -> Calcula o fatorial de um número.
    :param numero: O número a ser calculado
    :param show: (opcional) mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    valor = 1
    for i in range(numero, 0, -1):
        if show == 1:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        valor *= i
    if show == 0:
        print('Não mostrarei o cálculo.')
    return valor


numero = int(input('Informe o número que deseja saber o fatorial: '))
show = int(input('Deseja ver o cálculo [0/1]? '))
if show != 1 and show != 0:
    show = int(input('Opção inválida, digite 0 para não informar e 1 para informar conta: '))
print(fatorial(numero, show))

'''help(fatorial)'''