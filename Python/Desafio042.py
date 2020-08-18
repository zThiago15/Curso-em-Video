cores = {'limpar':'\033[m', 'vermelho':'\033[1;31m','ciano':'\033[1;36m','azul':'\033[1;34m','amarelo':'\033[1;33m','verde':'\033[1;32m'}

print('===== Tipo de Triângulo -> Aprimoramento do Desafio 35 =====')
print()
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < s2+s3 and s2 < s1+s3 and s3 < s1+s2:
    print(f'{(cores["verde"])}PODE {(cores["limpar"])}se formar um triângulo! Do tipo:')

    if s1 == s2 == s3: #Se forem os 3 segmentos iguais
        print(f'{(cores["amarelo"])}EQUILÁTERO! {(cores["limpar"])}(Todos os lados são iguais).')

    elif s1 != s2 != s3 != s1: #Se forem 3 segmentos diferentes
        print(f'{(cores["azul"])}ESCALENO! {(cores["limpar"])}(Todos os lados diferentes).')

    else: #Se forem 2 segmentos iguais e 1 diferente
        print(f'{(cores["ciano"])}ISÓSCELES! {(cores["limpar"])}(Dois lados iguais).')
else:
    print(f'{(cores["vermelho"])}NÃO PODE {(cores["limpar"])}se formar um triângulo!')