cores = {'limpar':'\033[m','amarelo':'\033[33m','azul':'\033[34m','verde':'\033[32m'}

n1 = float(input('\033[1;33mPrimeira nota do aluno(a): '))
n2 = float(input('\033[1;34mSegunda nota do aluno(a): '))
média = (n1+n2)/2
print(f'{(cores["limpar"])}A média entre {(cores["amarelo"])}{n1:.1f} {(cores["limpar"])}e {(cores["azul"])}{n2:.1f} {(cores["limpar"])}fica {(cores["verde"])}{média:.1f}!')