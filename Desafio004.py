a = input('Digite algo aí: ')

print('\033[1;30mO seu tipo primitivo é: ', type(a))
print('\033[1;34mSó tem espaços?', a.isspace())
print('\033[1;33mSó tem número?', a.isnumeric())
print('\033[1;32mSó tem letra?', a.isalpha())
print('\033[1;31mÉ alphanumérico?', a.isalnum())
print('\033[1;35mÉ um dígito?', a.isdigit())
print('\033[1;36mÉ só maiúsculo?', a.isupper())
print('\033[1;37mÉ só minúsculo?', a.islower())
print('\033[1;34mEstá capitalizado?', a.istitle())
print('\033[1;31mPode ser impresso', a.isprintable())
