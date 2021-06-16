nome = str(input('\033[033mDigite seu nome completo: ')).strip()
print('\033[1;36m1° método: Seu nome tem Silva?\n','Silva' in nome.title())
print('\033[1;30m=-'*20)

print('\033[1;34m2° método: Seu nome tem Silva?','silva' in nome.lower())
