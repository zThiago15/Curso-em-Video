cores = {'branco':'\033[30m','amarelo':'\033[33m','azul':'\033[34m','limpar':'\033[m','ciano':'\033[36m','vermelho':'\033[31m'}



n = int(input('\033[1;30mDigite um número: '))
print(f'{(cores["limpar"])}O dobro de {(cores["azul"])}{n} {(cores["limpar"])}vale {(cores["amarelo"])}{n*2} {(cores["limpar"])}O triplo de {(cores["azul"])}{n} {(cores["limpar"])}vale {(cores["ciano"])}{n*3}!')
print(f'{(cores["limpar"])}E a raiz quadrada de {(cores["azul"])}{n} {(cores["limpar"])}é igual a {(cores["vermelho"])}{pow(n,1/2):.2f}!')