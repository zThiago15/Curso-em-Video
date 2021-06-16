print('===== Alistamento Militar =====')
print()
from datetime import date #Importando data.
sexo = str(input('Você é homem ou mulher? ')).title().strip()

if sexo == 'Mulher':
    print('Você não precisa fazer o alistamento militar obrigatório.') #Se for mulher.

elif sexo == 'Homem': #Se for homem.

    nascimento = int(input('Em que ano você nasceu? '))
    atual = date.today().year #Ano atual
    idade = atual - nascimento #Quantos anos você tem.

    if idade < 18 and nascimento <= atual: #Se você é menor que 18 anos.
        print(f'Quem nasceu em {nascimento} têm {idade} anos em {atual}.')
        print(f'Faltam ainda {18 - idade} ano(s) para você se alistar.') #Quantos anos faltam.
        print(f'Seu alistamento será em {nascimento + 18}.') #Em que ano será seu alistamento.

    elif idade == 18: #Se você tem ou fará 18 nesse ano.
        print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}')
        print(f'Está na hora de você se alistar IMEDIATAMENTE!')

    elif idade > 18: #Se você já passou dos 18 anos.
        print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}.')
        print(f'Você já deveria ter se alistado a {idade - 18} ano(s) atrás.') #A quantos anos você deveria ter se alistado.
        print(f'Seu alistamento foi em {nascimento + 18}.') #Ano em que se alistou ou deveria ter se alistado.

    elif nascimento > atual: #Se a pessoa colocar um ano maior que o ano atual.
        print(f'Você veio do futuro é??? Nem chegamos em {nascimento} ainda haha')
        print(f'Por favor, tente novamente!')

else: #Caso a pessoa tenha digitado algo errado.
    print('Você digitou algo errado! Tente novamente.')