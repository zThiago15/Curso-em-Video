print('\033[30mEx: Digite um nome de uma cidade e mostre se ela começa com SANTO.')
print('\033[1;31m=-'*20)

cid = str(input('\033[1;34mDigite o nome da cidade em que você nasceu: '))
div = cid.split()
print('1° método: Começa com Santo?','Santo'  in div[0].title())
print('2° método: Começa com SANTO?', div[0].upper() == 'SANTO')