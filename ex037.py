num = int(input('Digite um número inteiro: '))
print('-=' * 20)
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
print('-=' * 20)
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    num_binario = bin(num)
    num_binario = num_binario[2:]
    print('O número decimal {} em binário fica {}'.format(num, num_binario))
elif opcao == 2:
    num_octal = oct(num)
    num_octal = num_octal[2:]
    print('O número decimal {} em octal fica {}'.format(num, num_octal))
elif opcao == 3:
    num_hex = hex(num)
    num_hex = num_hex[2:]
    print('O número decimal {} em hexadecimal fica {}'.format(num, num_hex))
else:
    print('Opção inválida. Tente novamente.')
