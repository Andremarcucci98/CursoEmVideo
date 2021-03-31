#Crie um programa que leia o nome completo de uma pessoa e mostre :
#O nome com todas as letras maiúsculas;
#O nome com todas minúsculas;
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome
print('======== Desafio 22 ========')
nome = str(input('Digite o nome completo: ')).strip()
print(nome)
nomeupper = nome.upper()
print ('Nome tudo em maiúsculo: ',nomeupper)
nomelower = nome.lower()
print('Nome tudo em minúsculo: ', nomelower)
print('Numero de letras sem espaço: {} '.format(len(nome) - nome.count(' ')))
dividido = nome.split()
print('Seu primeiro nome é {} o qual possui {} letras '.format(dividido[0],len(dividido[0])))