n = int(input('Quantos termos da sequência de Fibonacci deseja ver? '))
c = 1
t1 = 0
t2 = 1

print('{}'.format(t1), end='=')
print('{}'.format(t2), end='=')

while c <= n:
    t3 = t1 + t2
    print('{}'.format(t3), end='=')
    t1 = t2
    t2 = t3
    c += 1

print(' FIM')
