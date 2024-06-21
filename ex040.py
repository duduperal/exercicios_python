# Coleta os dados das notas
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
# Calcula a média
m = (n1 + n2) / 2

# Print de quanto o aluno tirou na n1 na n2 e sua média
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, m))

# Checa se o aluno está aprovado, de recuperação, ou reprovado
if m < 5:
    print('REPROVADO!')
elif m <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO!')
