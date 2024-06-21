from time import sleep
cinquenta = vinte = dez = um = 0
print('-------------------------')
print('          ATM')
print('------------------------')
valor = int(input('Digite o valor a ser sacado: R$'))
print('CALCULANDO...')
print('------------------------')
sleep(2)
while valor >= 50:
    cinquenta += 1
    valor -= 50
while 50 > valor >= 20:
    vinte += 1
    valor -= 20
while 20 > valor >= 10:
    dez += 1
    valor -= 10
while 10 > valor >= 1:
    um += 1
    valor -= 1
print(f'Total de {cinquenta} de R$50')
print(f'Total de {vinte} de R$20')
print(f'Total de {dez} de R$10')
print(f'Total de {um} de R$1')
print('--------------------------')
print('OBRIGADO, VOLTE SEMPRE!')
