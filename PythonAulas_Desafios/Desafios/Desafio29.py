from termcolor import colored
print('-=-'*10,'Desafio 29','-=-'*10)
v = float(input('Digite sua velocidade: '))
if v > 80.0:
    print('Você está acima da velocidade permitida, portanto será multado!!')
    multa = (v - 80)*7.0
    print('Sua multa será de R${:.2}'.format(multa))
else:
    print(colored('Parabéns por contribuir com uma direção segura','yellow'))