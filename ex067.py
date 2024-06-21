while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-='*20)
    if n < 0:
        print('TABUADA ENCERRADA!')
        break
    else:
        for i in range (1, 11):
            print(f'{n} x {i:2} = {n*i}')
    print('-='*50)
