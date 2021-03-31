print('{:=^40}'.format(' Desafio48 '))
n = int(input('Digite um numero entre 1 e 500: '))
s = 0
if 1<= n <= 500:
    print('Muito bem... Você digitou {}'.format(n))
    if (n % 2) == 1:
        for c in range (0, n+1, 3):
            if (n % 3) == 0:
                if (c % 2) == 1:
                    print(c)
                    s += c
        print('A soma dos numeros ímpares e múltiplos de 3 de {} possui o valor {}'.format(n, s))
    if (n % 2) == 0:
        for c in range (0,n+1,3):
            if (c % 3) == 0:
                if (c % 2) == 1:
                    print(c)
                    s+= c
        print('A soma dos numeros ímpares e múltiplos de 3 de {} possui o valor {}'.format(n, s))

else:
    print('Você digitou um numero fora do intervalo pedido.')