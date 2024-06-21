n = int(input('Digite o número que você deseja ver a tabuada: '))
print('-=' * 20)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, (n * c)))