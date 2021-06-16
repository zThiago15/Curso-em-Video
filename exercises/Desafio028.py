from random import randint #randint pega um numero aleatorio inteiro
from time import sleep
print('\033[1;33m===== JOGO DA ADIVINHAÇÃO =====')
print('\033[33m-=-'*20)
print('\033[1;34mVou pensar em um número de 0 à 5. Tente adivinhar...')
print('\033[33m-=-'*20)
pc = randint(0,5) #Faz o computador pensar em um número entre 0 até 5
jogador = int(input('\033[30mEm qual número eu pensei? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(1) #Esperar 1 segundo
if jogador == pc:
    print(f'\033[1;32mParabéns, você me venceu!Eu pensei no número \033[1;34m{pc} \033[1;32me você no \033[1;34m{jogador} \033[1;33mtambém!')
else:
    print(f'\033[31mGANHEI! EU pensei no número \033[1;34m{pc} \033[31me não no \033[1;34m{jogador}.')
print('\033[1;30mFim do  jogo!')
print('\033[33m-=-'*20) #Dá pra fazer esse exercício usando o from random import choice tbm