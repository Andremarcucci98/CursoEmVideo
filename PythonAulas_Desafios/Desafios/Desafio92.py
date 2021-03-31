pessoa = dict()
from datetime import datetime
pessoa['Nome'] = str(input('Nome: ')).strip()
nasc = int(input('Ano de nascimento: '))
pessoa['Idade'] = datetime.now().year - nasc
pessoa['CTPS'] = int(input('Carteira de trabalho (0 não tem):'))
if pessoa['CTPS'] != 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$ '))
    pessoa['Aposentadoria'] = pessoa['Idade'] + ((pessoa['Ano de contratação'] +35) - datetime.now().year)
print('-='*30)
for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')