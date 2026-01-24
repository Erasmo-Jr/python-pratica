from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Anos de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contatação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contatação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  -{k} tem o valor {v}')
