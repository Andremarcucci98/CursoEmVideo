print('Controle de terrenos')
print('====================')
def area(a ,b):
    area = a * b
    print(f'A área de {a:.2f}m x {b:.2f}m = {area:.2f}m^2')


comprimento = float(input('Digite o comprimento (m): '))
largura = float(input('Digite a largura (m): '))
area(comprimento, largura)