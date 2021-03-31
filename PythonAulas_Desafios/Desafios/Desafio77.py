tupla = ('Palavra', 'Caneca', 'Caneta',
         'Fone', 'Celular', 'Controle',
         'Curso', 'Video', 'Playstation')
for s in tupla:
    print(f'\nNa palavra {s.upper()} temos: ', end='')
    for vogal in s:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')