frase = str(input('\033[31mDigite uma frase de seu agrado: ')).upper().strip()
print('\033[1;33mA letra "A" aparece', frase.count('A'),'vezes na sua frase.')
print('\033[1;34mO  primeiro "A" apareceu na posição', frase.find('A'))
print('\033[1;32mO último "A" apareceu na posição', frase.rfind('A'))