num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 > num2 and num1 > num3:
    print('O primeiro número {} é maior que o {} e o {}'.format(num1, num2, num3))
elif num2 > num1 and num2 > num3:
    print('O segundo número {} é maior que o {} e o {}'.format(num2, num1, num3))
else:
    print('O terceiro número {} é maior que o {} e o {}'.format(num3, num1, num2))