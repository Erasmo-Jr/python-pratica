def área(larg, comp):
    a = larg * comp
    print(f'A ára de um terreno {larg}m x {comp}m é {a}m²')


#Programa Principal
print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)