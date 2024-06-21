from datetime import date
# Pega o sexo da pessoa e formata para maiusculo e tira os espaços indesejáveis
print('-=' * 20)
print('Digite "F" para feminino')
print('Digite "M" para masculino')
print('-=' * 20)
sexo = str(input('Digite aqui: '))
sexo = sexo.strip().upper()

# Pega o ano de nascimento da pessoa e calcula a idade de acordo com o ano atual
nasc = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

# Checa se a pessoa é do sexo masculino ou feminino
if sexo == 'M':
    
    # Checa de acordo com a idade se ainda tem que se alistar, se já passou da época, ou se está na época
    if idade < 18:
        falta = 18 - idade
        print('Ainda faltam {} anos para você se alistar'.format(falta))
        print('Seu alistamento será em {}.'.format(nasc + 18))

    elif idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    else:
        passou = idade - 18
        print('Você já deveria ter se alistado à {} anos.'.format(passou))
        print('Seu alistamento foi em {}.'.format(nasc + 18))
elif sexo == 'F':
    print('Você não precisa fazer o alistamento militar obrigatório, Tenha um bom dia senhora!')
