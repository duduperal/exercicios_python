from datetime import date

# Pega a idade do atleta e calcula a idade de acordo com o ano atual
ano_atual = date.today().year
ano = int(input('Insira o ano de nascimento do atleta: '))
idade = ano_atual - ano
print('O atleta tem {} anos.'.format(idade))

# Checa a idade com a determinada classificação de atletas
if idade <= 9:
    print('Atleta Mirim!')
elif idade <= 14:
    print('Atleta Infantil!')
elif idade <= 19:
    print('Atleta Junior!')
elif idade <= 25:
    print('Atleta Sênior!')
elif idade > 25:
    print('Atleta Master!')
