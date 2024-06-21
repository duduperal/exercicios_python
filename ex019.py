from random import randint
num = randint(1, 4)
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

if num == 1:
    print("O aluno escolhido foi {}".format(aluno1))
elif num == 2:
    print("O aluno escolhido foi {}".format(aluno2))
elif num == 3:
    print("O aluno escolhido foi {}".format(aluno3))
else:
    print("O aluno escolhido foi {}".format(aluno4))

