maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('-=' * 20)
print('O maior peso lido foi: {:.1f}Kg'.format(maior))
print('O menor peso lido foi: {:.1f}Kg'.format(menor))