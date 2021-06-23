import re


def main():
    ass_main = le_assinatura()
    textos_main = le_textos()
    caso_copiah = avalia_textos(textos_main, ass_main)
    print(f'O autor do texto {caso_copiah} esta infectado com COH-PIAH. ')



def le_assinatura():

    """A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada
    com os textos fornecidos"""
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))
    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    """A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento"""
    i = 1
    textos = []
    texto = input("\nDigite o texto " + str(i) +
                  "(aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("\nDigite o texto " + str(i) +
                      "(aperte enter para sair):")
    return textos


def separa_sentencas(texto):
    """A funcao recebe um texto e devolve uma lista das sentencas dentro do texto"""
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    """A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca"""
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    """A funcao recebe uma frase e devolve uma lista das palavras dentro da frase"""
    return frase.split()


def n_palavras_unicas(lista_palavras):
    """Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez"""
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    """Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas"""
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    """IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade
    nas assinaturas."""
    similaridade = 0
    for i in range(0, 6):
        valor = as_a[i] - as_b[i]
        if valor < 0:
            valor = valor * (-1)
        similaridade += valor
    return similaridade / 6


def calcula_assinatura(texto):
    """IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto."""

    sentencas = separa_sentencas(texto)
    dict_frases = []
    tamanho_sentenca = 0
    for i in sentencas:
        tamanho_sentenca += len(i)
        dict_frases.append(separa_frases(i))

    list_frases = []
    for j in dict_frases:
        for k in j:
            list_frases.append(k)

    tamanho_frase = 0
    for i in list_frases:
        tamanho_frase += len(i)

    dict_palavras = []
    for j in dict_frases:
        for k in j:
            dict_palavras.append(separa_palavras(k))

    list_palavras = []
    for j in dict_palavras:
        for k in j:
            list_palavras.append(k)
    soma_tamanho_palavras = 0
    for i in list_palavras:
        soma_tamanho_palavras += len(i)

    numero_frases = len(list_frases)
    # print(f'Numero de dict_frases: {numero_frases}')
    numero_sentencas = len(sentencas)
    # print(f'Numero de sentenças: {numero_sentencas}')
    total_palavras = len(list_palavras)
    # print(f'Total de palavras: {total_palavras}')
    palavras_unicas = n_palavras_unicas(list_palavras)
    # print(f'Palavras unicas: {palavras_unicas}')
    palavras_diferentes = n_palavras_diferentes(list_palavras)
    # print(f'Palavras diferentes: {palavras_diferentes}')
    # print(f'Soma dos tamanhos das palavras: {soma_tamanho_palavras}')

    list_ass_texto = []
    list_ass_texto.append(soma_tamanho_palavras / total_palavras)
    list_ass_texto.append(palavras_diferentes / total_palavras)
    list_ass_texto.append(palavras_unicas / total_palavras)
    list_ass_texto.append(tamanho_sentenca / numero_sentencas)
    list_ass_texto.append(numero_frases / numero_sentencas)
    list_ass_texto.append(tamanho_frase / numero_frases)

    # Tamanho médio de palavra
    # tamanho_medio_palavra = soma_tamanho_palavras / total_palavras
    # print(f'Tamanho médio de palavra: {tamanho_medio_palavra}')

    # Relação Type-Token
    # type_token = palavras_diferentes / total_palavras
    # print(f'Relação Type-Token: {type_token}')

    # Razão Hapax Legomana
    # hapax_legomana = palavras_unicas / total_palavras
    # print(f'Razão Hapax Legomana: {hapax_legomana}')

    # Tamanho Médio de Sentença
    # tamanho_medio_sentenca = tamanho_sentenca / numero_sentencas
    # print(f'Tamanho médio de sentença: {tamanho_medio_sentenca}')

    # Complexidade de sentença
    # complexidade_sentenca = numero_frases / numero_sentencas
    # print(f'Complexidade de sentença: {complexidade_sentenca}')

    # Tamanho médio de frase
    # tamanho_medio_frase = tamanho_frase / numero_frases
    # print(f'Tamanho médio de frase: {tamanho_medio_frase}')

    return list_ass_texto


def avalia_textos(textos, ass_cp):
    """IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n)
    do texto com maior probabilidade de ter sido infectado por COH-PIAH."""
    assinaturas = []
    for i in textos:
        assinaturas.append(calcula_assinatura(i))
    numeracao_texto = -1
    grausimilaridade = 6
    for i in range(0, len(assinaturas)):
        similaridade = compara_assinatura(ass_cp, assinaturas[i])
        if i == 0:
            grausimilaridade = similaridade
        elif i > 0:
            if similaridade < grausimilaridade:
                grausimilaridade = similaridade
                numeracao_texto = i + 1
    return numeracao_texto


main()