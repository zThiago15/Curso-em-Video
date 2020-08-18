frase = 'Curso em Vídeo Python'

print('FATIAMENTO DE STRING')
print()

print('===== Análise =====')
print()

print(frase[:15])
print(frase[::3])
print(frase[5:15:2])
print(f'A frase {frase} têm', len(frase),'caracteres')
print(frase.count('o',0,15))
print(frase.find('s'))
print('Curso' in frase)
print()

print('===== Transformação =====')
print()

print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
print()

print('===== Divisão =====')
print(frase.split())
print()

print('===== Junção =====')
print(''.join(frase))
print()

print('MISTURANDO')
print(frase.upper().find('VÍDEO'))
print(frase.replace('Python','Jogos').find('Jogos'))
print(frase.split(),'-'.join(frase))
dividido = frase.split()
print('-'.join(dividido))
print()

print('OBS: Pra fazer uma junção melhor com o .join(),')
print('Coloque o método .split() em uma variável. Ex: "divisão = frase.split()"')
print()

print(frase.lower().find('vídeo'))
print(frase.upper().find('PYTHON'))
print(frase.replace('Python','oooooo').count('o',0,21))
print(frase.upper().count('O'))
print(frase.upper().replace('PYTHON','Android'))
print()


frase2 = 'Gosto muito de programação! Principalmente Python.'
divisão = frase2.split()
print(f'A frase dividida ficou {divisão}. Ao juntarmos ficará:','.'.join(divisão))
print(divisão[1][1])
print(divisão[3][5])
print(divisão[5][4])