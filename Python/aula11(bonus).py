''''#\033[0;33;44m ---> \033[(style);(text);(back)m
print('\033[0;30;41mTeste1')
print('\033[4;33;44mTeste2')
print('\033[1;35;43mTeste3')
print('\033[30;42mTeste4')
print('\033mTeste4') #--> Desfaz as configurações e volta pro padrão(letra cinza e fundo preto)
print('\033[7;30mTeste5'), --> O 7 inverte a cor do fundo e da letra, ou
seja, se eu colocar a letra 30(branca) o 7 vai inverter com a cor padrão que é preto
e deixar o branco de fundo e o preto da cor da letra.'''

print('\033[1;4;30;41mOlá, Mundo!\033[m')
print('\033[1;33m=-\033[m'*20)
a = 3
b = 40
print(f'Os valores são:\033[1;33m{a}\033[m e \033[1;31m{b}\033[m!!!')
print('\033[33m=-'*20)
print()
#Cores
cores =  {'limpar':'\033[m',
#{(cores["limpar"])}
            
            'branco':'\033[30m',
#{(cores["branco"])}
         
         'vermelho':'\033[31m',
#{(cores["vermelho"])}       
         
         'verde':'\033[32m',
#{(cores["verde"])} 
         
         'amarelo':'\033[33m',
#{(cores["amarelo"])}       
        
         'azul':'\033[34m',
#{(cores["azul"])}         
        
        'roxo':'\033[35m',
#{(cores["roxo"])}       
        
         'ciano':'\033[36m',
#{(cores["ciano"])}         
         
         'cinza':'\033[37m',
#{(cores["cinza"])}         
         

# cores em negrito

'vermelho em negrito': '\033[1;31m',
'azul em negrito': '\033[1;34m',
'amarelo em negrito': '\033[1;33m',
'branco em negrito': '\033[1;30m',
'roxo em negrito': '\033[1;35m',
'verde em negrito': '\033[1;32m',
'ciano em negrito': '\033[1;36m',

# cores sublinhadas

'vermelho sublinhado': '\033[4;31m',
'azul sublinhado': '\033[4;34m',
'amarelo sublinhado': '\033[4;33m',
'branco sublinhado': '\033[4;30m',
'roxo sublinhado': '\033[4;35m',
'verde sublinhado': '\033[4;32m',
'ciano sublinhado': '\033[4;36m'}

nome = input('Qual é o seu nome? ')
print(f'{(nome["azul"])}Muito prazer em te conhecer, {(nome["vermelho"])}!!!')