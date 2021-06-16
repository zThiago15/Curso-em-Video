soma = 0 #Acumulador
contador = 0#Contador

for c in range(1, 501, 2):#Vai de 1 até 500 pulando de 2 em 2(Ou seja, pegando só os números ímpares)

    if c % 3 == 0:#Se o número dentro desse intervalo for divisível por 3

        soma += c #Acumula todos os números (nesse caso, está somando). Ex: 5 e 8 = a soma vale 13
        contador += 1#Pra cada valor dentro desse intervalo ele soma 1. Ex: 5 e 8 = São 2 valores
print(f'São {contador} valores e a soma de todos esses valores valem: {soma}!')