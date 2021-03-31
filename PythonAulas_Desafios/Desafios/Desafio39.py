print('=-='*5, 'Alistamento', '=-='*5)
import datetime
idade = int(input('Digite seu ano de nascimento: '))
alistamento = datetime.date.today()
ano = alistamento.year
escolha = str(input('Já se alistou!? Digite y para sim e n para não: '))
if escolha == 'n':
    if (ano - idade) < 18:
        print('Você ainda não precisa de alistar.')
        tempo_alist = (18 - (ano - idade)) * 12
        print('Para se alistar, será necessário esperar um período de {} meses.'.format(tempo_alist))
    elif (ano - idade) == 18:
        print('Você deve se alistar na unidade mais próxima.')
    elif (ano - idade) > 18:
        print('Procure uma unidade o mais rápido possível.')
elif escolha == 'y':
    print('Contamos com sua ajuda nas forças armadas.')