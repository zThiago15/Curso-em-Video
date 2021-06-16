from datetime import date
print('===== Confederação Nacional de Natação =====')
print()
cores = {'limpar':'\033[m','branco':'\033[1;30m','vermelho':'\033[1;31m','verde':'\033[1;32m','amarelo':'\033[1;33m','azul':'\033[1;34m'}
nascimento = int(input('Informe o ano em que você nasceu: '))
tempo = date.today().year
idade = tempo - nascimento

if idade <= 9:
    print(f'O atleta tem {(cores["branco"])}{idade} {(cores["limpar"])}anos. Sua categoria é: {(cores["branco"])}MIRIM')

elif idade <= 14:
    print(f'O atleta tem {(cores["azul"])}{idade} {(cores["limpar"])}anos. Sua categoria é: {(cores["azul"])}INFANTIL')

elif idade <= 19:
    print(f'O atleta tem {(cores["vermelho"])}{idade} {(cores["limpar"])}anos. Sua categoria é: {(cores["vermelho"])}JÚNIOR')

elif idade <= 25:
    print(f'O atleta tem {(cores["verde"])}{idade} {(cores["limpar"])}anos. Sua categoria é: {(cores["verde"])}SÊNIOR')

else:
    print(f'O atleta tem {(cores["amarelo"])}{idade} {(cores["limpar"])}anos. Sua categoria é: {(cores["amarelo"])}MASTER')