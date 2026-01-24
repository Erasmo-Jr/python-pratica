while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    print('-' * 30)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num*c}')
    print('-'*30)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')




