# DESAFIO GARAIIII
nome = str(input('Digite seu nome: ')).strip()
dividor = nome.split()
print('ANALISANDO...')
print('MAIÚSCULAS: {}'.format(nome.upper()))
print('minúsculas: {}'.format(nome.lower()))
print('Quantas letras sem espaço: {}'.format(len(nome) - nome.count(' ')))
print('Quantas letras tem o primeiro nome: {}'.format(len(dividor[0])))
