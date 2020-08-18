'''
for c in range(0,7,2): #Vai de 0 até 6 (porque ele ignora o último número) pulando de 2 em 2.
    print(c)
print('FIM')

n = int(input('Digite um número aí vlh: '))
for sla in range (0,n+1): #Vai ir até o número que a pessoa escolheu.
    print(sla)
print('FIM')

for eitaporra in range(0,1001,100): #Vai de 0 até 1000 pulando de 100 em 100
    print(eitaporra)
print
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i, f+1, p):#c é de contador, ele vai contar do número 1 até o número que a pessoa escolheu
    print(c)
print('Fim')

soma = 0
for c in range(0,3):
    n = int(input('Digite um número: '))
    soma += n'''

#print(f'A soma dos 10 números foram {soma}')

s = 0 #Acumulador(Vai somar todos os números)
c = 0 #Somador (Soma cada valor como 1)
for c in range(0,101,50): #'c' é de contador, ele vai contar de um número até algum número
    print(c)
    s += c
print(f'A soma é {s} e o tanto de valores colocados são {c}')