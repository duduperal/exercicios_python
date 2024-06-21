vel = float(input('Qual a velocidade atual do carro: '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você foi multado em R${:.2f}'.format(multa))
else:
    print('Você não foi multado')