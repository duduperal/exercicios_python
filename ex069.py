homens = mulheres_menos_20 = mais_18 = 0
while True:
    opcao = ' '
    sexo = ' '
    print('-------------------------')
    print(f'  CADASTRO DE PESSOA')
    print('-------------------------')
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
    if idade >= 18:
        mais_18 += 1
    if opcao == 'N':
        break
print('-=' * 30)
print(f'Total de pessoas maiores de idade: {mais_18}')
print(f'Total de homens : {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres_menos_20}')
print('-=' * 30)
