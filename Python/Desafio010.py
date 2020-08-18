r = float(input('\033[30mQuantos reais você tem na carteira? R$'))
da = r*0.24
dc = r*0.32
dau = r*0.36
eu = r*0.22
print(f'Com \033[34mR${r} \033[30mvocê pode comprar \033[33m${da:.2f} \033[30mem dólares americanos,')
print(f'\033[33m${dc:.2f} \033[30mem dólar canadense,\033[33m${dau:.2f} \033[30mem dólar australiano.')
print(f'E \033[33m${eu:.2f} \033[30mem euro.')
print('Considerando o valor a partir de 31/06/2019')
