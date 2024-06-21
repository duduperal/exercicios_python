sal = float(input('Digite o seu salário: R$'))
if sal > 1250:
    salnovo = sal + (sal * 10 / 100)
else:
    salnovo = sal + (sal * 15 / 100)
print('O seu salário novo é de R${:.2f}'.format(salnovo))
