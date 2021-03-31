nome = str(input('Qual seu nome? '))
if nome == 'Andre':
    print('Muy bien!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem comum no Brasil.')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome')
else:
    print('Muy malo!!')
print('Tenha um bom dia {}'.format(nome))