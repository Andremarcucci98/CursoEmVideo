from time import sleep


def contador(inicio, fim, p):
    print('-='*20)
    print(f'Contagem de {inicio} até {fim} de {p} em {p}')
    sleep(0.3)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
        print(f'Que pena,vou tomar seu tempo fazendo a contagem de {inicio} até {fim} de {p} em {p} ')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            cont += p
            sleep(0.3)
        print('FIM')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont -= p
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('=-'*20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
