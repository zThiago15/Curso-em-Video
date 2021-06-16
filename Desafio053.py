#Sem usar 'for'
print('===== Verificação de Palíndromo =====')#Título
print()#Pular linha
cores = {'vermelho':'\033[1;31m','amarelo':'\033[1;33m'}#Cores
frase = str(input('Digite  uma frase: ')).replace(' ','').lower() #Digitar uma frase
contr = frase[::-1]#Frase ao contrário
print(f'A frase "{frase.upper()}" ao contrário é "{contr.upper()}".')#Como ela fica ao contrário
if frase == contr:#Se ela for a mesma coisa ao contrário
    print(f'{(cores["amarelo"])}Essa frase é um palíndromo!')
else:#Se não for, não é palíndromo
    print(f'{(cores["vermelho"])}Essa frase não é um palíndromo!')
print()

#Usando estrutura de repetiçaõ 'for'
'''print('Usando a estrutura de repetição "for"')
cores = {'limpar':'\033[m','vermelho':'\033[1;31m','amarelo':'\033[1;33m'}
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'A frase {(cores["amarelo"])}É {(cores["limpar"])}um palíndromo!')
else:
    print(f'A frase {(cores["vermelho"])}NÃO {(cores["limpar"])}É um palíndromo!')'''