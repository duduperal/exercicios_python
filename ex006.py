n = int(input("Digite um número: "))
d = n * 2
t = n * 3
raizq = n ** 0.5
print('\033[1;36;45mO dobro de {} vale {}.\033[m'.format(n, d))
print('\033[1;31;45mO triplo de {} vale {}.\033[m'.format(n, t))
print('\033[7;40mA raiz quadrada de {} é igual a {:.2f}\033[m'.format(n, raizq))
