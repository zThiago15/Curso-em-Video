from datetime import date #Importando a biblioteca de data
atual = date.today().year #Calculando o ano de hoje
mai = 0 #maioridade
men = 0 #menor
c = 0 #somador
for niver in range(0,7):
    c += 1
    nas = int(input(f'Em que ano a {c}ª você nasceu? '))
    idade = atual - nas
    if idade >= 21:
        mai += 1
    else:
        men += 1
print(f'Ao todo, {mai} pessoas são maiores de idade')
print(f'E {men} pessoas são menores de idade.')