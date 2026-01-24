numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não vou adicionar!')
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn': #Se a resposta for Nn o programa para e mostra o resultado
        break
print('-='*30)
numeros.sort() #Deixa os valores finais em ordem numericas
print(f'Você digitou os valores {numeros}')