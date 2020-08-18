somador = 0
contador = 0
for c in range(1,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        somador += n
        contador += 1
print(f'Foram informados {contador} número(s) PAR(ES) e a soma foi: {somador}!')