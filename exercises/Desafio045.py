from random import choice
from time import sleep
cores = {'limpar':'\033[m','vermelho':'\033[1;31m','verde':'\033[1;32m','amarelo':'\033[1;33m','azul':'\033[1;34m', 'ciano':'\033[1;36m'}

print(f'{(cores["ciano"])}=-'*10,f'{(cores["ciano"])}JOKENPÔ',f'{(cores["ciano"])}=-'*10) #Layout(estética)
print()
jogador = str(input('''\033[1;30mOpções de Jogada:
[Pedra], [Papel] e [Tesoura]
Qual a sua escolha? ''')).lower().strip() #Escolha do jogador

movimentos = ['pedra', 'papel', 'tesoura']
pc = choice(movimentos) #Escolha do computador

print(f'{(cores["azul"])}JO')
sleep(0.5) #Tempo de espera
print(f'{(cores["azul"])}KEN')
sleep(0.5)
print(f'{(cores["azul"])}PÔ!!!')

print('=-'*20)#Layout(estética)
if jogador == 'tesoura' or jogador == 'pedra' or jogador == 'papel': #Se o jogador digitar certo alguma opção.

    if jogador == 'pedra' and pc == 'tesoura' or jogador == 'papel' and pc == 'pedra' or jogador == 'tesoura' and pc == 'papel': #Se o jogador ganhar
        print(f'{(cores["verde"])}Parabéns! Você ganhou!!! {(cores["limpar"])}O computador escolheu {(cores["vermelho"])}{pc} {(cores["limpar"])}e você {(cores["amarelo"])}{jogador}!')

    elif jogador == pc: #Se o jogo empatar
        print(f'{(cores["ciano"])}EMPATE! {(cores["limpar"])}Você escolheu {(cores["azul"])}{jogador} {(cores["limpar"])}e o computador {(cores["azul"])}{pc} {(cores["limpar"])}também!')

    else: #Se o jogador perder
        print(f'{(cores["vermelho"])}Você PERDEU! {(cores["limpar"])}O computador escolheu {(cores["verde"])}{pc} {(cores["limpar"])}e você {(cores["vermelho"])}{jogador}!')

else: #Se o jogador digitar algo errado
    print(f'{(cores["vermelho"])}Você digitou algo errado, tente novamente!')
print(f'{(cores["azul"])}=-'*20)#Layout(estética)