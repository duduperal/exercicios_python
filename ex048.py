s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print('-=' * 26)
print('A soma de todos os {} valores solicitados é {}'.format(cont, s))
print('-=' * 26)
