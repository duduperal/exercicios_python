from random import randint
tot = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um valor: '))
    jogada = str(input('Par ou ímpar? [P/I]: ')).upper().strip()[0]
    total = computador + jogador
    print('-=' * 30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} DEU PAR')
    if jogada not in 'PI':
        print('JOGADA ÍNVALIDA TENTE NOVAMENTE!')
        break
    if jogada == 'I' and total % 2 == 0:
        print(f'GAME OVER! Você venceu {tot} vezes.')
        break
    if jogada == 'P' and total % 2 != 0:
        print(f'GAME OVER! Você venceu {tot} vezes.')
        break
    if jogada == 'P' and total % 2 == 0:
        print(f'Você venceu!')
        print(f'Vamos jogar novamente!')
        tot += 1
    if jogada == 'I' and total % 2 != 0:
        print(f'Você venceu!')
        print(f'Vamos jogar novamente!')
        tot += 1
print('-=' * 30)