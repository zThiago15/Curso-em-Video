from datetime import date
ano = int(input('\033[30mQual ano você quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year #Ele irá analisar o ano atual e dizer se ele é bissexto ou não.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[1;30mO ano \033[1;34m{ano} \033[30mÉ BISSEXTO.')
else:
    print(f'\033[31mO ano \033[1;34m{ano} \033[31mNÃO é BISSEXTO.')
print('\033[34m='*15,'Fim do PROGRAMA','='*15)