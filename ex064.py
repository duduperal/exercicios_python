cont = 0
soma = 0
num = int(input('Digite um valor: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um valor: '))
print('Você digitou {} valores.'.format(cont))
print('E a soma desses valores é igual a: {}'.format(soma))
