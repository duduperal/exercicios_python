from random import randint
tot = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um valor: '))
    jogada = ' '
    total = computador + jogador
    while jogada not in 'PI':
        jogada = str(input('Par ou ímpar? [P/I]: ')).upper().strip()[0]
    print('-=' * 30)
    if total % 2 == 0:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total} DEU PAR')
    else:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total} DEU ÍMPAR')
    if jogada == 'P':
        if total % 2 == 0:
            print(f'VOCÊ GANHOU')
            tot += 1
        else:
            print(f'VOCÊ PERDEU')
            break
    elif jogada == 'I':
        if total % 2 == 1:
            print(f'VOCÊ GANHOU')
            tot += 1
        else:
            print(f'VOCÊ PERDEU')
            break
print(f'GAME OVER! Você venceu {tot} vezes')
print('-=' * 30)
