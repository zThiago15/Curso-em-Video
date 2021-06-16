cores = {'limpar':'\033[m','verde':'\033[1;32m','azul':'\033[1;34m','amarelo':'\033[1;33m','ciano':'\033[1;36m','vermelho':'\033[1;31m'}

print('='*20,'LOJA','='*20)
print()
preço = float(input('Qual o valor do produto? R$'))
condição = str(input('Qual a forma de pagamento?(Dinheiro, boleto, cartão) ')).title().strip()

if condição == 'Dinheiro' or condição == 'Boleto':
    desconto = preço - (preço * 10 / 100)
    print(f'Escolhendo pagar no {(cores["amarelo"])}{condição}, {(cores["limpar"])}você terá um desconto de 10%! Passando a pagar {(cores["verde"])}R${desconto:.2f}!')

if condição == 'Cartão':
    vezes = int(input('Em quantas vezes no cartão?(Até 2x sem juros!) '))
    if vezes == 1:
        desconto = preço - (preço * 5 / 100)
        print(f'Escolhendo pagar no {(cores["azul"])}{condição} {(cores["limpar"])}à vista, você terá um desconto de {(cores["amarelo"])}5%! {(cores["limpar"])}Passando a pagar {(cores["ciano"])}R${desconto:.2f}!')
    elif vezes == 2:
        print(f'Irá ficar o preço normal, em 2x de {(cores["verde"])}R${preço/2}!')
    elif vezes >= 3:
        juros = preço + (preço * 20 / 100)
        dividido = juros / vezes
        print(f'Parcelando em {(cores["azul"])}{vezes}x {(cores["limpar"])}irá ter {(cores["amarelo"])}20% de juros no valor total, {(cores["limpar"])}ficando por {(cores["amarelo"])}R${juros:.2f} {(cores["limpar"])}e pra cada parcela fica {(cores["azul"])}R${dividido:.2f}!')
else:
    print(f'{(cores["vermelho"])}Forma de pagamento inválida. Tente novamente!')

cores = {'limpar':'\033[m','amarelo':'\033[33m','azul':'\033[34m'}
preço = float(input('Qual o preço do produto? '))
forma = str(input('Qual a forma de pagamento?(Dinheiro/cheque/cartão)')).title().strip()
if forma == 'Dinheiro' or forma == 'Cheque':
    desconto = preço - (preço * 10/100)
    print(f'À vista no {(cores["azul"])}{forma} vai ter um desconto de 10%, ficando por {(cores["amarelo"])}R${desconto}!')
if forma == 'Cartão':
    vezes = int(input('Em quantas vezes no cartão? '))
    if vezes == 1:
        desconto = preço (preço * 5 / 100)
        print(f'Você terá um desconto de 5%, passando a pagar por {(cores["amarelo"])}R${desconto}!')
    elif vezes == 2:
        print(f'Você irá pagar {(cores["amarelo"])}{preço/2}!')
    elif vezes > 2:
        juros = preço + (preço * 20 / 100)
        print(f'Você terá 20% de juros, passando a pagar {(cores["amarelo"])}R${juros/vezes}!')
else:
    print('Forma de pagamento inválida! Por favor, tente novamente!')