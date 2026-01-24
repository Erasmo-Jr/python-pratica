palavra = ('Jogos', 'Games', 'Monitor', 'Joystick', 'Mouse', 'Instagran', 'Mago')

for p in palavra:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')