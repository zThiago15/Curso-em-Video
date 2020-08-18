nome = str(input('Qual é o seu primeiro nome? ')).title().strip()
print()
if nome == 'Thiago':
    print(f'Que nome lindo você tem {nome}! :D')
    print('Tenha uma ótima tarde!')
else:
    print('Sério? Que nome comum...')
    print('Mesmo assim, boa tarde.')
print()


print('Vamos calcular sua média!')
print()

n1 = float(input('Qual a sua primeira nota? '))
n2 = float(input('Qual a segunda? '))
n3 = float(input('A terceira? '))
n4 = float(input('E a quarta? '))
nu = (n1+n2+n3+n4)/4
print(f'Sua média final foi {nu:.1f}')
if nu >= 6:
    print('Sua média foi boa. PARABÉNS!')
else:
    print('Sua média não foi boa. ESTUDE MAIS!')
print()

print('===== FIM =====')