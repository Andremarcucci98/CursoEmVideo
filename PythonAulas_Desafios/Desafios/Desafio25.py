nome = str(input('Digite seu nome completo: ')).strip()
#print('Voce possui "SILVA" no nome? {}'.format('SILVA' in nome.upper()))
nome1 = nome.upper().split()
print('Voce possui "SILVA" no nome? {} '.format('SILVA' in nome1))