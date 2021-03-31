print('\033[7;33;44mOlá, Mundo!\033[m')
a = 3
b = 8
print('Os valores são \033[7;33m{}\033[m e \033[7;34m{}\033[m !!'.format(a,b))
nome = 'Andre'
print('Olá, muito prazer em te conhecer {}{}{}'.format('\033[4;34m', nome, '\033[m'))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretobranco':'\033[7:30m'}
print('Olá, muito prazer em te conhecer {}{}{}'.format(cores['pretobranco'], nome, cores['limpa']))