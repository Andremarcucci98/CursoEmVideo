def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg).replace(',','.'))
        except (ValueError, TypeError):
            print('\033[3;31mERRO: Digite um número float válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mOUsuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um número Inteiro: ')
n2 = leiaFloat('Digite um Real: ').replace(',','.')
print(f'Você acabou de digitar o número inteiro {n1} e o número real {n2}')