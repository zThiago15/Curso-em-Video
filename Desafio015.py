dias = int(input('\033[31mPor quantos dias o carro está alugado? '))
km = float(input('Quantos Km rodados? '))
total = (dias * 60) + (km * 0.15)
print(f'\033[30mO total a ser pago são \033[1;32mR${total:.2f}')