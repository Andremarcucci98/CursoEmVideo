print('=-='*5,'Desafio 43','=-='*5)
from time import sleep
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
print('PROCESSANDO', end='', flush=True)
sleep(0.5)
print('.', end='', flush=True)
sleep(0.5)
print('.', end='', flush=True)
sleep(0.5)
print('.',end='',flush=True)
imc = peso / (altura * altura)
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif 18.5 < imc <= 25:
    print ('Você está no peso ideal.')
elif 25 < imc <= 30:
    print('Você está com sobrepeso.')
elif 30 < imc <= 40:
    print('Você está com sobrepeso.')
elif imc > 40:
    print('Você está com obesidade mórbida.')