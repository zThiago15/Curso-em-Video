cores = {'limpar':'\033[m','vermelho':'\033[1;31m','verde':'\033[1;32m','azul':'\033[1;34m','branco':'\033[1;30m'}
print('===== Cálculo de IMC =====')
print()
sexo = str(input('Sexo[M/F]: ')).upper().strip()
peso = float(input('Quanto você pesa?(Kg) '))
altura = float(input('Qual a sua altura?(m) '))
IMC = peso / (altura ** 2) #Dois asteríscos são exponenciação. Nessa caso, estão 2 elevado ao quadrado.

#Abaixo do peso(M e F)
if IMC < 20 and sexo == 'M':
    print(f'Seu IMC vale {IMC:.2f}! Você está {(cores["vermelho"])}abaixo do peso! Cuidado!')
elif IMC < 19 and sexo == 'F':
    print(f'Seu IMC vale {IMC:.2f}! Você está {(cores["vermelho"])}abaixo do peso! Cuidado!')

#Peso normal(M e F)
elif 20 <= IMC < 25 and sexo == 'M':
    print(f'Seu IMC vale {IMC:.2f}! O seu peso é o {(cores["verde"])}IDEAL! {(cores["limpar"])}Parabéns!')
elif 19 <= IMC < 24 and sexo == 'F':
    print(f'Seu IMC vale {IMC:.2f}! O seu peso é o {(cores["verde"])}IDEAL! {(cores["limpar"])}Parabéns!')

#Sobrepeso(M e F)
elif 25 <= IMC < 30:
    print(f'Seu IMC vale {IMC:.2f}! Você está com {(cores["azul"])}Sobrepeso!')
elif 24 <= IMC < 29:
    print(f'Seu IMC vale {IMC:.2f}! Você está com {(cores["azul"])}Sobrepeso!')

#Obesidade(M e F)
elif 30 <= IMC < 40:
    print(f'Seu IMC vale {IMC:.1f}! Você está com {(cores["branco"])}Obesidade!')
elif 29 <= IMC < 39:
    print(f'Seu IMC vale {IMC:.2f}! Você está com {(cores["branco"])}Obesidade!')

#Obesidade Mórbida(M e F)
elif IMC >= 40:
    print(f'Seu IMC vale {IMC:.2f}! Você está com {(cores["vermelho"])}Obesidade mórbida! Cuidado!')
elif IMC >= 39:
    print(f'Seu IMC vale {IMC:.2f}! Você está com {(cores["vermelho"])}Obesidade mórbida! Cuidado!')