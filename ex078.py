listanum = [] #Lista
maior = 0
menor = 0
for c in range (0, 5): #Contador de 0 até 4
    listanum.append(int(input(f'Digite um valor para  a posição {c}: '))) #Adicionando um inteiro na lista
    if c == 0: #Encontrando maior e menor valor
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for indice, valor in enumerate(listanum): #Numerando as posições dos inteiros
    if valor == maio:
        print(f'{indice}... ', end='')
print() #Serve para quebra de linha
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for indice, valor in enumerate(listanum):
    if valor == menor:
        print(f'{indice}...', end='')
print()
print('=-'*30)
