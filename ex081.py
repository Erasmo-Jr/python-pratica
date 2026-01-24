valores = []
while True:
    valores.append(int(input('Digite um valor: '))) #Adicionando valores
    resp = str(input('Quer continuar? [S/N] ')) #Condição de repetição se quer continuar
    if resp in 'Nn': #Se a resposta for Nn encerra o programa e mostra os resultados abaixo
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos') #Mostra quantos elementos foram digitados
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores: #Verifica se o valor 5 ta na lista
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')