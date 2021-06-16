print('Usando "min" e "max"!')  # Usando os objetos min e max
lista = []  # Adc uma lista vazia

for p in range(1, 6):  # Vai de 1 até 5

    peso = float(input(f'Qual é o peso da {p}ª pessoa?(Kg) '))#Vai adc 1 pra cada pessoa
    lista += [peso]  # A lista vai receber o peso das pessoas

print(f'O maior peso é {max(lista)}Kg')  # Max vai reconhecer o maior peso da lista
print(f'E o menor peso é {min(lista)}Kg!')  # Min vai reconhecer o menor peso da lista


#Método do professor
maior = 0
menor = 0
#Maior e menor vão ser 0

for p in range(1,6): #Vai de 1 à 5
    peso = float(input(f'Qual é o peso da {p}ª pessoa?(Kg) '))#Adc 1 pra cada pessoa
    if p == 1: #O maior e menor vão ser iguais ao peso da primeira pessoa
        maior = peso
        menor = peso
    else:
        if peso > maior:#Se tiver um peso maior q a 1ª pessoa, então o maior vai ser ele
            maior = peso
        elif peso < menor:#Se tiver um peso menor q o da 1° pessoa, então o menor vai ser ele
            menor = peso
print(f'O maior peso é {maior}Kg')#O maior peso
print(f'O menor peso é {menor}Kg')#O menor peso