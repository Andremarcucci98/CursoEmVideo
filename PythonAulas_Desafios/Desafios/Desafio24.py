print('======== Desafio 24 ========')
nome = str(input('Digite o nome da cidade: ')).strip().capitalize()
#if (nome[:5] == 'Santo'):
#   print('A cidade começa com "Santo"')
#else:
#    print('A cidade não começa com "Santo"')]
print('A cidade começa com Santo? {}'.format('Santo' in nome[0:5]))