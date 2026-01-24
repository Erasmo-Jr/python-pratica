from time import sleep


def maior(*num):
    cont = maior = 0
    print('\nAnalisando os dados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
    print(f'Foram encontrado {cont} valores ao todo.')
    print(f'O maior valor foi {maior}.')



#Programa Principal
maior(5, 6, 23, 55, 101)
maior(2, 222)
maior(7)
maior()