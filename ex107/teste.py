import moeda
#from moeda import metade, dobro, aumentar -> assim economiza memoria
#from ex107 import moeda -> assim também funciona
p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é R${moeda.metade(p)}')
print(f'o dobro de {p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')