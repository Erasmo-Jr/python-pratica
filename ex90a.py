aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Media do {aluno['Nome']}: '))
if aluno['Média'] >= 7:
    aluno['Média'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Média'] = 'Recuperação'
else:
    aluno['Média'] = 'Reprovado'
for v, i in aluno.items():
    print(f' {v} = {i}')
