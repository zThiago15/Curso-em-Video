cores = {'vermelho':'\033[1;31m', 'verde':'\033[1;32m', 'azul':'\033[1;34m','limpar':'\033[m','amarelo':'\033[1;33m','ciano':'\033[1;36m'}

número = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
base = int(input('Qual é a sua opção: '))

if base == 1:
    print(f'O número {(cores["verde"])}{número} {(cores["limpar"])}convertido para BINÁRIO é igual a {(cores["azul"])}{bin(número)[2:]}') #BINÁRIO

elif base == 2:
    print(f'O número {(cores["verde"])}{número} {(cores["limpar"])}convertido para OCTAL é igual a {(cores["amarelo"])}{oct(número)[2:]}') #OCTAL

elif base == 3:
    print(f'O número {(cores["verde"])}{número} {(cores["limpar"])}convertido para HEXADECIMAL é igual a {(cores["ciano"])}{hex(número)[2:]}') #HEXADECIMAL 
else:
    print(f'{(cores["vermelho"])}Você digitou errado! Tente novamente.')