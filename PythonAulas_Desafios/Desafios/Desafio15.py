km = float(input('Digite a quantidade de quilômetros rodados pelo carro: '))
d = int(input('Digite a quantidade de dias alugados: '))
f = km * 0.15
a = d * 60
total = a + f
print(f'O valor pago de aluguel foi de R$ {a :.2f} \no valor pago por distância percorrida foi de R$ {f :.2f} \no que da um total de R$ {total :.2f} ')