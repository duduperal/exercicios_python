# Pega o valor da compra e a opção de pagamento
print('{:=^40}'.format(' SUPERMERCADO2000 '))
valor = float(input('Qual o preço das compras? R$'))
print('[ 1 ] para à vista no dinheiro/cheque')
print('[ 2 ] para à vista no cartão')
print('[ 3 ] para 2x no cartão')
print('[ 4 ] para 3x ou mais no cartão')
print('-=' * 22)
opcao = int(input('Qual a opção? '))
print('-=' * 22)

# Checa as opções de pagamento e faz os devidos calculos
if opcao == 1:
    total = valor - (valor * 10 / 100)
elif opcao == 2:
    total = valor - (valor * 5 / 100)
elif opcao == 3:
    total = valor
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format((valor / 2)))
elif opcao == 4:
    parcel = int(input('Quantas parcelas? '))
    total = valor + (valor * 20 / 100)
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcel, (total / parcel)))
else:
    print('Opção ínvalida, tente novamente!')
print('O valor a ser pago será de R${:.2f}'.format(total))

print('-=' * 22)
