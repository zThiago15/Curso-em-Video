num = int(input('Digite um número: '))#Variável
tot = 0 #Somador
for contador in range(1, num + 1):#Ele vai contar de 1 até o número escolhido

    if num % contador == 0:#Se o numero dividido pelo contador for igual a zero
        print('\033[33m', end='')#Vai deixar os numeros divisíveis com a cor amarela
        tot += 1#Soma 1 pra cada divisor

    else:#Se não der 0(Se não for divisível)
        print('\033[31m', end='')#Deixa com a cor vermelha

    print(contador, end=' ')#Vai printar todos os números e deixar com as cores acima

print(f'\n\033[mO número {num} foi divisível {tot} vezes!')#Vai ver quantas vezes ele foi divisível
if tot == 2:
    print('Ele É um número primo!')#Se for divisível só 2 vezes, então é primo.
else:
    print('Ele NÃO É um número primo!')#Se não for divisível 2 vezes não é primo.