salário = float(input('\033[34mQual é o seu salário? R$'))
if salário > 1250: #Quem ganha mais de 1250 aumenta só 10 % o salário.
    novo = salário + (salário * 10 / 100)
    print(f'Você irá ter 10% de aumento, passando a ganhar \033[1;33mR${novo:.2f}!')
else:  #Quem ganha menos de 1250 aumenta 15%.
    novo = salário + (salário * 15 / 100)
    print(f'Você irá ter um aumento de 15%, passando a ganhar \033[1;33mR${novo:.2f}!')