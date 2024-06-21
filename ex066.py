tot = s = 0
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    else:
        tot += 1
        s += n
print('-=' * 30)
print(f'Foram digitados {tot} números e a soma entre eles foi {s}')
