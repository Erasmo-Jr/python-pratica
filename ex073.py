times = ('Corinthians', 'Palmeiras', 'Santos',
         'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco',
         'Chapecoense', 'Atlético', 'Botafogo',
         'Atlético-PR', 'Bahia', 'São Paulo',
         'Fluminense', 'Sport Recife', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-='*15)
print(f'Lista de times do Brasileirão: {times}')
print('-='*15)
print(f'Os 5 primeiros times são {times[0:5]}')
print('-='*15)
print(f'Os últimos 4 colocados são {times[-4:]}')
print('-='*15)
print(f'Os time em ordem alfabética são{sorted(times)}')
print('-='*15)
print(f'O time da Chapecoense está na {times.index('Chapecoense')+1}ª posição')