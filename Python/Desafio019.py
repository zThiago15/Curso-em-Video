from random import choice
a1 = str(input('\033[34mPrimeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
sorteio = [a1, a2, a3, a4]
print(f'\033[30mO(a) aluno(a) sorteado(a) para apagar a lousa será o(a): \033[33m{choice(sorteio)}')