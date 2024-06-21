valcasa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o sálario do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = valcasa / (anos*12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valcasa, anos, prestacao))
if sal * 30 / 100 < prestacao:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')