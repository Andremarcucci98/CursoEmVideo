aluno = {}
sala = []
num = int(input('Quantos alunos gostaria de cadastrar? '))
for c in range(0,num):
    aluno['nome'] = str(input('Nome: '))
    aluno['media'] = float(input('Média: '))
    while aluno["media"] > 10:
        aluno['media'] = float(input('Digite a média correta: '))
    if aluno["media"] >= 5:
        aluno['situacao'] = 'Aprovado'
    else: aluno['Situacao'] = 'Reprovado'
    sala.append(aluno.copy())
    print('-'*20)
print('-='*20)
print(f'{"Nome":<4}   {"Média":<20}{"Situação":>10}')
print('-='*20)
for i in range(0,num):
    print(f'{sala[i]["nome"]:<4}   {sala[i]["media"]:<20}{sala[i]["situacao"]:>10}')
print('-='*20)