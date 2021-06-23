n = int(input('Digite um numero: '))
unidade = n % 10
dezena = ((n - unidade)/10) % 10
print(f'O dígito das dezenas é {dezena:.0f}')