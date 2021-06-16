from math import radians, sin, cos, tan
angulo = float(input('\033[1;32mDigite um ângulo: '))
seno = sin(radians(angulo))
print(f'O valor do SENO é: \033[1;33m{seno:.2f}')
cosseno = cos(radians(angulo))
print(f'\033[1;32mO valor do COSSENO será: \033[1;33m{cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'\033[1;32mO valor da tangente será: \033[1;33m{tangente:.2f}')