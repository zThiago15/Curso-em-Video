co = float(input('\033[1;30mCateto oposto: '))
ca = float(input('Cateto adjacente: '))
h = (co**2)+(ca**2)
print(f'A hipotenusa vai valer:\n\033[1;34m{h**(1/2):.2f}')

print('\033[1;33m=-'*20)
print ('\033[34mOutro método')

from math import hypot
co = float(input('\033[33mDigite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hyp = hypot(co,ca)
print(f'Agora a hipotenusa vai valer: \033[1;32m{hyp:.2f}')