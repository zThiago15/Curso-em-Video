'''print('Exemplo!')
nome = str(input('Qual é o seu nome? ')).title().strip()
if nome == 'Thiago':
    print('Que nome bonito!')
elif nome == 'Giovanna' or nome == 'Rafaella'or nome == 'Ingrid':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia {nome}!')
print()'''
'''condições aninhadas == várias estrutures condicionais'''

#'else' pode ser usado uma ou nenhuma vez enquanto o 'elif'pode ser usado
#quantas vezes quiser!

nome = str(input('OPA! Tudo bem com vocês! Qual é o seu nome?? ')).title().strip()
if nome == 'Thiago':
    print('Caraca, seu nome é muito lindo!')
elif nome == 'João' or nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é muito popular no Brasil!')
elif nome in 'Ana Bianca Rafaela Izabella Pietra':
    print('Belo nome feminino! :D')
else:
    print('Seu nome é beeeeeem normal!')
print(f'Tenha uma boa tarde, {nome}!')
