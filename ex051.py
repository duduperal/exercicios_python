pt = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão dessa PA: '))
dec = pt + (10 - 1) * razao
print('-=' * 10)
for c in range(pt, dec + 1, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')