p = float(input('\033[33mDigite o preço de um produto: R$'))
d = p-(p*5/100)
print(f'\033[34mO novo preço com 5% de desconto vai ficar por \033[32mR${d:.2f}!')
