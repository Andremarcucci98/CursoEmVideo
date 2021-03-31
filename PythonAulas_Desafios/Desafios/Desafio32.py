from termcolor import colored
from datetime import date
print('-=-'*5,'Desafio 32','-=-'*5)
ano = int(input('Digite um ano qualquer, vamos analisar se ele é bissexto.Caso queira analisar o ano tual digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {}',colored('NÃO','red'), 'é bissexto'.format(ano))