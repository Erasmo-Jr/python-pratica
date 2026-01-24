from time import sleep
from random import randint
from operator import itemgetter
jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}

ranking = [] #Criando novo lista para organizar ordem

print('valores sorteados:')
for k, i in jogo.items():
    print(f'{k} tirou {i} no dado.')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('~'*5, end='')
print(' RANKING DOS JOGADORES ', end='')
print('~'*5)
print()
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
print()
print(f'Parabéns ao {ranking[0][0]} pela 1º posição no Ranking!')