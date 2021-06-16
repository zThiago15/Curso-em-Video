from emoji import emojize
from time import sleep
print('===== Estouro de Fogos de Artifício! =====')
cores = {'vermelho':'\033[31m','amarelo':'\033[33m'}
for r in range (10,-1,-1):
    print(r)
    sleep(0.5)
print(f'{(cores["amarelo"])}ESTOURO DE FOGOS DE ARTIFÍCIO!!! BUUM! POOW! ')
print(emojize(f'{(cores["vermelho"])}:sparkles: '*10))