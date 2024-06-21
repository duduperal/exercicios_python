n1 = float(input('Digite o 1 valor: '))
n2 = float(input('Digite o 2 valor: '))
opcao = 0
while opcao != 5:
    print('-=' * 20)
    print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA''')
    print('-=' * 20)
    opcao = int(input('Digite a sua escolha: '))
    if opcao == 1:
        print('{} + {} = {}'.format(n1, n2, (n1+n2)))
    elif opcao == 2:
        print('{} x {} = {}'.format(n1, n2, (n1*n2)))
    elif opcao == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n1 < n2:
            print('{} é menor que {}'.format(n1, n2))
        else:
            print('Eles são iguais!')
    elif opcao == 4:
        print('-=' * 20)
        n1 = float(input('Digite o 1 valor: '))
        n2 = float(input('Digite o 2 valor: '))
        print('-=' * 20)
    elif opcao == 5:
        opcao = 5
    else:
        print('Escolha INVÁLIDA')
