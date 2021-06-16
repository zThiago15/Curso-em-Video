real1 = float(input('\033[35mDigite um número real: '))
print(f'O número \033[34m{real1} \033[35mtem a parte inteira de:\n\033[34m{int(real1)}')

print('\033[33m=-'*20)
print ('\033[34mOutro método')

from math import trunc
real2 = float(input('Digite outro número real: '))
print(f'O número \033[31m{real2} \033[34mtem uma porção inteira de:\n\033[31m{trunc(real2)}')