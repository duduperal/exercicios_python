total = mais_mil = preco_mais_barato = 0
cont = 1
nome_mais_barato = ''
print('--------------------------------')
print('       SUPERMERCADO2000')
print('--------------------------------')
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço deste produto: R$'))
    opcao = ' '
    total += preco
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cont == 1:
        preco_mais_barato = preco
    if preco > 1000:
        mais_mil += 1
    if preco <= preco_mais_barato:
        preco_mais_barato = preco
        nome_mais_barato = produto
    if opcao == 'N':
        break
    cont += 1
print('-=' * 30)
print(f'O total gasto na compra foi {total}')
print(f'{mais_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_mais_barato.capitalize()} custando {preco_mais_barato}')
