from random import shuffle
a1 = str(input('\033[1;32mPrimeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
sorteio = [a1, a2, a3, a4]
shuffle(sorteio)
print(f'\033[34mA ordem de apresentação dos alunos será: \033[1;33m{sorteio}')