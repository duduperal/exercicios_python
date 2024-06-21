n = int(input('Digite um número: '))
print('-=' * 20)
tot = 0
if n <= 1:
    print('\033[41mNão existem números primos menores que 1!\033[m')
else:
    for i in range(1, n + 1):
        if n % i == 0:
            print('\033[31m', end=' ')
            tot += 1
        else:
            print('\033[33m', end=' ')
        print('{}'.format(i), end=' ')
    print('\n\033[mO número {} foi divisível {} vezes'.format(n, tot))
    if tot > 2:
        print('E por isso ele não é PRIMO!')
    else:
        print('E por isso ele é PRIMO!')