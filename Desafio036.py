'''cores = {'vermelho':'\033[31m','verde':'\033[32m','limpar':'\033[m'}

casa = float(input('Valor da casa? R$'))
salário = float(input('Qual seu salário mensal? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12) #Quanto irá pagar pela casa por mês dentro desse tempo
mínimo = salário * 30 / 100 #Quanto é 30% do salário que não pode exceder
print(f'Para pagar uma casa de R${casa} em {anos} anos',end='')
print(f' a prestação mensal será de R${prestação:.2f}')
if prestação <= mínimo: #Se a prestação for menor ou igual aos 30% do salário, o empréstimo é aprovado
    print(f'{(cores["verde"])}Empréstimo aprovado!')
else: #Se a prestação for maior que 30% do salário, então é negado
    print(f'{(cores["vermelho"])}Empréstimo negado!')
print(f'{(cores["limpar"])}Comparando: Tem que pagar R${prestação:.2f} por mês e o mínimo é R${mínimo:.2f}')'''

cores = {'limpar':'\033[m','vermelho':'\033[31m','azul':'\033[34m','amarelo':'\033[33m'}
casa = float(input('Qual é o valor da casa? R$'))
salário = float(input('Qual é o salário mensal? R$'))
anos = int(input('Por quantos anos irá pagar? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print(f'Para pagar uma casa de {(cores["azul"])}R${casa} {(cores["limpar"])}durante {(cores["azul"])}{anos}',end='')
print(f'{(cores["limpar"])} anos, você irá pagar {(cores["azul"])}{mínimo} {(cores["limpar"])}por mês!')
if prestação > mínimo:
    print(f'{(cores["vermelho"])}Empréstimo negado! {(cores["limpar"])}Você não pode financiar essa casa.')
else:
    print(f'{(cores["amarelo"])}Empréstimo aprovado! {(cores["limpar"])}Você irá pagar R${mínimo} por mês!')