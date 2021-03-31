n = int(input('Digite um número: '))
print('-=-'*5,'Analisando paridade','-=-'*5)
resto = n % 2
if resto == 0 :
    print('Seu numero é PAR')
else:
    print('Seu numero é ÍMPAR')