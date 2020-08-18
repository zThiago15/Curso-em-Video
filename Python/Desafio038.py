cores = {'limpar':'\033[m','verde':'\033[1;32m'}
#{(cores["verde"])}
#{(cores["limpar"])}

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo: '))
if n1 > n2:
    print(f'O PRIMEIRO valor é o {(cores["verde"])}maior!')
elif n2 > n1:
    print(f'O SEGUNDO valor é o {(cores["verde"])}maior!')
else:
    print(f'Não existe valor maior, {(cores["verde"])}os dois são IGUAIS!')