'''A repetição While é: Ex - Enquanto n chegar na maça, dar passo

for c in range(1,10):
    print(c)
print('FIM')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Você quer continuar?[S/N] ')).upper()
print('FIM')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} númeors ímpares!')