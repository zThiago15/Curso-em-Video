nome = str(input('\033[1;36mDigite seu nome completo: ')).strip()
print('Seu nome em letras maiúsculas é', nome.upper())
print('Seu nome em letras minúsculas é', nome.lower())

print('\033[1;30mAo todo, seu nome têm', '\033[34m',len(nome.replace(' ','')), '\033[1;30mletras.')

#print('Ao todo, seu nome têm', len(nome) - nome.count(' '),'letras.')

print('\033[31mTESTE')
divisão  = nome.split()
print('Seu primeiro é',(divisão [0]),'e têm', len(divisão[0]),'letras.')


print(f'Seu primeiro nome é',divisão[0],'e têm',nome.find(' '),'letras.')