from random import randint
random = randint(0, 5)
print('--=--' * 10)
print(' ' * 3, 'Pensando tente adivinhar...', ' ' * 3)
print('--=--' * 10)
num = int(input('Digite um número entre 0 e 5: '))
if num == random:
    print('O computador escolheu {} e você também escolheu {} então você ganhou!'.format(random, num))
else:
    print('O computador escolheu {} e você {} então você perdeu! Tente novamente!'.format(random, num))
