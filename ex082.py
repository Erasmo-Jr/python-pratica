valores = []
par = []
impar = []
while True:
    valores.append(int(input('Digite um valor: ')))
    cond = str(input('Quer continuar? [S/N] '))
    if cond in 'Nn':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'A lista completa é {valores}')
print(f'A lista com valores pares é {par}')
print(f'A lista com valores ímpares é {impar}')
