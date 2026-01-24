n1 = float(input('Qual a primeira nota: '))
n2 = float(input('Qual a segunda nota: '))
m = (n1 + n2) / 2
#Lembrar da ordem de precedencia dos parenteses
print('A media entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, m))
#com apenas um digito usar {:.1f}