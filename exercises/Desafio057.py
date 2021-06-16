sexo = input("Qual seu sexo?")
while sexo in 'FM':
    print('Qual seu sexo?[F/M] ')
    if sexo != 'F' or sexo != 'M':
        print('Você digitou errado! Tente novamente.')