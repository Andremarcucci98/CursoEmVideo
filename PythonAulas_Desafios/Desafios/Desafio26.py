#Ler frase e falar quantos "A" aparecem, em que posição aparece a primeira e ultima vezes
f = str(input('Digite uma frase: ')).strip().upper()
print('Na frase digitada existem {} "As"'.format(f.count('A')))
print('Na frase digitada aparece primeiramente na posição {} e ultimamente na posição {} '.format(f.find('A')+1, f.rfind('A')+1))
