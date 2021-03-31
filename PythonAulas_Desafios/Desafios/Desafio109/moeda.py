def aumentar(preço = 0, taxa = 0, formato=False):
    '''

    :param preço: valor dado pelo usuário
    :param taxa: taxa que vai somar ou subtrair valor preço
    :param formato: formata o valor final para notação monetária
    :return: retorna o valor final
    '''
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço = 0, taxa = 0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço = 0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço = 0, formato=False):
    res = preço/2
    return res if formato is False else moeda(res)


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')