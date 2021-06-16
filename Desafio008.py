cores = {'branco':'\033[30m','vermelho':'\033[31m','amarelo':'\033[33m'}

m = float(input('\033[32mDigite uma distância em metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
c = m*100
mm = m*1000
print(f'{(cores["branco"])}A medida de {(cores["vermelho"])}{m}m {(cores["branco"])}equivale a:\n{(cores["amarelo"])}{km:.2f}km \n{(cores["amarelo"])}{hm:.2f}hm \n{(cores["amarelo"])}{dam:.2f}dam \n{(cores["amarelo"])}{dm:.2f}dm \n{(cores["amarelo"])}{c:.2f}cm \n{(cores["amarelo"])}{mm:.2f}mm')
