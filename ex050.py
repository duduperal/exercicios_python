s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('Você informou {} valores pares e a soma desses valores foi {}'.format(cont, s))