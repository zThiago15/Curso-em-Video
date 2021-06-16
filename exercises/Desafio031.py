distância = float(input('\033[34mQual é a distância da sua viagem? '))
print(f'\033[32mVocê está prestes a começar uma viagem de \033[1;33m{distância}Km.')

#Condição Composta
if distância <= 200:
    preço = distância * 0.50

else:
    preço = distância * 0.45
print(f'\033[32mE o preço da sua passagem será \033[1;33mR${preço:.2f}!')

#Condição simplificada
'''preço = distância * 0.50 if distância <= 200 else distância * 0.45
print(f'E o preço da sua viagem será de R${preço:.2f}!')'''