sexo = str(input('Digite o sexo da pessoa [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Porfavor, informe seu sexo: ')).upper().strip()[0]
if sexo == 'M':
    print('Sexo masculino registrado com sucesso.!')
elif sexo == 'F':
    print('Sexo feminino registrado com sucesso.!')