print('='*25)#Estética
print('10 TERMOS DE UMA PA')#Título
print('='*25)
termo = int(input('Qual é o primeiro termo: '))#Primeiro termo da PA
razão = int(input('Qual é a razão: '))#Razão da PA
s = 0 #Acumulador
for c in range(1,11):#Vai de 1 à 10
    s = termo + (c - 1) * razão #Fórmula da PA
    print(s, end= ('➡ '))#Resultado
print('ACABOU')
print()

print('Forma simplificada!')
num = int(input('Digite o Primeiro número da PA: '))
razão = int(input('Digite a Razão da PA: '))
for c in range(1, 11):
    print(num, end=' ')
    num += razão
print('Acabou')