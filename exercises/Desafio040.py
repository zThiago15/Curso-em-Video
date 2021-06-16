cores = {'vermelho':'\033[1;31m', 'azul':'\033[1;34m','verde':'\033[1;32m'}

n1 = float(input('Qual foi sua primeira nota? ')) #Nota 1
n2 = float(input('Qual foi sua segunda nota? ')) #Nota 2
média = (n1 + n2) / 2 #Cálculo de média
print(f'Tirando {n1} e {n2} a sua média é {média:.1f}')
if média < 5.0: #Se for menor que 5
    print(f'O aluno está {(cores["vermelho"])}REPROVADO!')
elif 7 > média >= 5: #Se for maior que 4.9 e menor que 7
    print(f'O aluno está de {(cores["azul"])}RECUPERAÇÃO!')
elif média >= 7: #Se for maior ou igual a 7
    print(f'O aluno está {(cores["verde"])}APROVADO!')