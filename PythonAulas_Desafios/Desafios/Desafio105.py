'''def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 8:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

from random import randint
resp = notas(randint(1,10),randint(1,10),randint(1,10),randint(1,10), sit=True)
print(resp)
#help(notas)
choice = print('Gostaria de adicionar outro aluno [S/N]? ').upper().strip()
if choice == 'S':
    n = n+1
    resp = notas(randint(1,10),randint(1,10),randint(1,10),randint(1,10), sit=True)
print(resp)'''
from random import randint
def notas():
    no = []
    maior = t = 0
    menor = 10
    n = randint(1,10)
    for i in range(n):
        no.append(randint(1,10))
        if no[i] >= maior:
            maior = no[i]
        if no[i] <= menor:
            menor = no[i]
        t += no[i]
    r = dict()
    r['total'] = n
    r['maior nota'] = maior
    r['menor nota'] = menor
    r['média da turma'] = t/n
    choice = str(input('Você quer saber a situação da turma [S/N]? ')).upper().strip()
    if choice == 'S':
        if r['média da turma'] >= 8:
            r['situação'] = 'Muito boa'
        elif r['média da turma'] >= 6:
            r['situação'] = 'Boa'
        elif r['média da turma'] == 5:
            r['situação'] = 'Média'
        else:
            r['situação'] = 'Ruim'
    return r

print(notas())
