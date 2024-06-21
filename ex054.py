from datetime import date
maiores = 0
menores = 0
ano_atul = date.today().year
for i in range(1, 8):
    ano_nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(i)))
    idade = ano_atul - ano_nasc
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print('-=' * 20)
print('{} pessoas são maiores!'.format(maiores))
print('{} pessoas são menores!'.format(menores))
print('-=' * 20)