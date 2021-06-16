num = int(input('\033[1;32mDigite um número entre 0 e 9999: '))
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m = num//1000 % 10
print(f'\033[1;33mUnidade: \033[34m{u}')
print(f'\033[1;33mDezena: \033[34m{d}')
print(f'\033[1;33mCentena: \033[34m{c}')
print(f'\033[1;33mMilhar: \033[34m{m}')