print('-=-'*5,'\033[0;30;44m Desafio 36\033[m','-=-'*5)
casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int(input('Digite quantos anos serão necessários para pagá-la: '))
meses = anos * 12
prestacao = casa/meses
if prestacao <= (0.3 * salario):
    print('A prestação será de R${:.2f}'.format(prestacao))
    print('Parabéns!! Você \033[0;31m conseguirá\033[m financiar sua casa própria.')
else:
    print('A prestação será de R${:.2f}'.format(prestacao))
    print('Infelizmente o senhor \033[0;31m não conseguirá\033[m adquirir este apartamento, o empréstimo será negado.')