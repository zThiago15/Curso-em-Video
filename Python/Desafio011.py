l = float(input('\033[31mDigite a largura de sua parede: '))
al = float(input('\033[33mDigite a sua altura: '))
a = l*al
t = a/2
print(f'\033[mA sua parede tem uma dimensão de \033[34m{l:.2f} x {al:.2f} \033[me a sua área equivale a \033[34m{a:.2f}m².\nE precisará de \033[34m{t:.2f} litros de tinta para pintá-lá.')