print('====== DESAFIO 66 ======')
soma = cont = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Foram digitados {cont} numeros, cuja soma deu {soma}')