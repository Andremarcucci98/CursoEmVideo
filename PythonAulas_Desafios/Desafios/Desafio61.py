print('====== Desafio61 ======')
prim = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão: '))
cont = 1
prog = prim
total = 0
mais = 10
print('===Progressão Arit.===')
while mais !=0:
    total = total + mais
    while cont<= total:
        print('{} ->'.format(prog),end='')
        prog += razao
        cont +=1
    print('PAUSE')
    mais = int(input('Digite quantos termos a mais gostaria de adicionar: '))
print('Progressão finalizada com {} termos'.format(total))



