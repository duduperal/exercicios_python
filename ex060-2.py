from time import sleep
print('-=' * 20)
print('{:-^40}'.format('Cálculo De Fatorial'))
print('-=' * 20)
n = int(input('Digite um número: '))
c = n
f = 1

print('Calculando {}! '.format(n))
sleep(2)
while c > 0:
    print(c, end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f = f * c
    c -= 1
print(f)