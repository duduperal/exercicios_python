nota1 = float(input("Primeira nota do aluno: "))
nota2 = float(input("Segunda nota do aluno: "))
print("A média entre {}{:.2f}{} e {}{:.2f}{} é igual a {}{:.2f}{}".format('\033[31m', nota1, '\033[m', '\033[35m', nota2, '\033[m', '\033[40;33m', (nota1 + nota2) / 2, '\033[m'))
