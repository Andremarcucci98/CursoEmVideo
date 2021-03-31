print('=-='*5, 'Desafio 41','=-='*5)
import datetime
ano_nasc = int(input('Digite seu ano de nascimento, por favor: '))
ano_atual = datetime.date.today()
idade = (ano_atual.year) - ano_nasc
if (idade <= 9):
    print('Você está na categoria \033[0;31mMIRIM\033[m')
elif (9 < idade <= 14):
    print('Você está na categoria \033[0;31mINFANTIL\033[m')
elif (14 < idade <= 19):
    print('Você está na categoria \033[0;31mJUNIOR\033[m')
elif (19 < idade <= 20):
    print('Você está na categoria \033[0;31mSÊNIOR\033[m')
elif (idade > 20):
    print('Você está na categoria \033[0;31mMASTER\033[m')
print('Boa sorte na competição!!')