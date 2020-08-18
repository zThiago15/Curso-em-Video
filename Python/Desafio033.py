from time import sleep  # Espera alguns segundos antes de mostrar algo usando .sleep()

n1 = int(input('\033[33mPrimeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
# Verificando quem é o menor.
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando quem é o maior.
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('Analisando...')
sleep(1)
print(f'O menor número é: \033[34m{menor}.')
print(f'\033[33mO maior número é: \033[34m{maior}.')

print('\033[32m=-'*20)
print('\033[30mCalculando de forma simples.')
a = int(input('\033[30mDigite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
lista = [a, b, c]
print(f'O menor número é: \033[34m{min(lista)}.')
print(f'\033[30mO maior número é: \033[34m{max(lista)}.')
