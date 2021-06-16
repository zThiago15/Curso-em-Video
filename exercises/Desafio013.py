s = float(input('\033[1;30mDigite seu salário: R$'))
a = s+(s*15/100)
print(f'\033[1;32mSeu novo salário com um aumento de 15% vai ficar \033[36mR${a:.2f}')