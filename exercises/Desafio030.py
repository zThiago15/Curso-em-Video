número = int(input('\033[30mMe diga um número qualquer: '))
resultado = número % 2
print(f'O resto é {resultado}, logo:')
if resultado == 0: #Se o resto da divisão for igual a zero.
    print(f'O número \033[34m{número} \033[30mé PAR.')
else:
    print(f'O número \033[34m{número} \033[30mé ÍMPAR.')
#Se o resto da divisão do número divido por 2 for zero ele é par, se o resto da divisão der 1 ele é ímpar.
#Teste usando print(resultado)