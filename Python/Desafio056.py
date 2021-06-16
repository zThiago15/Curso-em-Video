maioridadehomem = 0 #Idade do homem mais velho
nomevelho = '' #Nome do homem mais velho
somaidade = 0 #Soma de todas as idadas
mulhermenor20 = 0 #Mulheres menores de 20 anos
for p in range(1,5):
    print(f'===== {p}ª PESSOA =====') #Posição da pessoa
    nome = str(input(f'Nome: ')).title().strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo[M/F]: ')).upper().strip()
    somaidade += idade #Somar as idades
    if sexo == 'M' and idade > maioridadehomem: #Se for homem e a idade for maior que 0
        maioridadehomem = idade #O homem mais velho recebe a idade
        nomevelho = nome #O homem mais velho recebe o nome
    elif sexo == 'F' and idade < 20: #Se for mulher e tiver menos que 20 anos
        mulhermenor20 += 1 #Vai adc 1
média = somaidade / 4 #Calcular a média
print(f'A média da idade do grupo é de {média} anos!')#A média da idade do grupo
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}!') #A idade e o nome do homemmais velho
print(f'{mulhermenor20} mulher(es) tem menos de 20 anos!') #Quantas mulheres tem menos de 20 anos