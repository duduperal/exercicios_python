opcao = 'S'
soma = tot = media = maior = menor = 0
while opcao in 'S':
    n = int(input('Digite um número inteiro: '))
    soma += n
    tot += 1
    if tot == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / tot
print('-=' * 30)
print('A média é {}'.format(media))
print('O menor é {}'.format(menor))
print('O maior é {}'.format(maior))
print('-=' * 30)
