dis = float(input('Digite a distância da viagem em KM: '))
if dis <= 200:
    custo = dis * 0.50
else:
    custo = dis * 0.45
print('Você está prestes a começar uma viage de {:.1f}Km.'.format(dis))
print('O preço da sua passagem é de R${:.2f}'.format(custo))