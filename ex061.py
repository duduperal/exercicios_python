print('-------------PROGRESSÃO ARITMÉTICA---------------')
pt = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razão da PA: '))
c = 1

while c <= 10:
    print(pt, end=' - ')
    pt += rz
    c += 1
print('FIM')