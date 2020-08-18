velocidade = float(input('\033[30mQual é a velocidade atual do carro? '))
multa = (velocidade-80)*7 #Multa de 7 reais por km excedido do limite
if velocidade > 80:
    print(f'\033[32mMULTADO! Você excedeu o  limite de 80km/h \nVai levar uma multa de \033[1;31mR${multa:.2f}!')
else:
    print('\033[1;32mMuito bem! Você não ultrapassou o limite de 80 km/h \nTenha um bom dia, dirija com segurança!')