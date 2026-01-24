temp = []
pessoas = []
pesado = leve = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        pesado = leve = temp[1]
    else:
        if temp[1] > pesado:
            pesado = temp[1]
        elif temp[1] < leve:
            leve = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break


print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')

print(f'O maior peso foi de {pesado}Kg Peso de ', end='')
for p in pessoas:
    if p[1] == pesado:
        print(f'{p[0]} ', end='')
print()
print(f'o menor peso foi de {leve}Kg Peso de ', end='')
for p in pessoas:
    if p[1] == leve:
        print(f'{p[0]} ', end='')
print()