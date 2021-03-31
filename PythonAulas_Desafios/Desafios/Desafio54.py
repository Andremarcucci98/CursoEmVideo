print('====== MAIORIDADE ======')
import datetime
atual = datetime.date.today()
print('Ano atual {}'.format(atual.year))
count = 0
for i in range(1,7):
    nasc = int(input('Digite seu ano de nascimento: '))
    if (atual.year - nasc) < 21:
        count += 1
print('{} ainda não atingiram a maioridade.'.format(count))




