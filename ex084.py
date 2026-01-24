temp = []
pessoas = []
leve = pesada = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        leve = pesada = temp[1]
    else:
        if temp[1] > pesada:
            pesada = temp[1]
        elif temp[1] < leve:
            leve = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]' ))
    if resp in 'Nn':
        break



print(f'{len(pessoas)} pessoas foram cadastradas!')

print(f'O menor peso foi de {leve}Kg Peso de ', end='')
for p in pessoas:
    if p[1] == leve:
        print(f'{p[0]} ', end='')
print()
print(f'O maior peso foi de {pesada}Kg Peso de ', end='')
for p in pessoas:
    if p[1] == pesada:
        print(f'{p[0]} ', end='')
print()
