from random import randint
from time import sleep

# Computador randomiza um numero de 0 a 10
computador = randint(0, 10)

# Print para "fingir" que o computador está pensando
print('----------= Jogo Da Adivinhação =----------')
print('O computador está pensando em um número...')
sleep(1)
print('hmmm')
sleep(1)
print('PENSEI!')
print('----------')
print('Tente adivinhar o número que eu pensei!')

# Váriavel que irá contar o total de jogadas feitas pelo jogador
total_jogadas = 0

# Váriavel de controle para quebrar o while loop
acertou = False

# Váriavel da jogada do jogador
jogador = 0

# While loop que vai ficar promptando qual o palpite e processando a jogada do jogador
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    print('Processando...')
    print('-' * 20)
    sleep(1)

    # Se a váriavel do jogador for == a do computador a variavel acertou recebe True encerrando o loop
    if jogador == computador:
        acertou = True

    # Se for diferente
    else:
        # Se a váriavel do jogador for menor que a do computador printar Mais...
        if jogador < computador:
            print('Mais...')

        # Senão printar Menos...
        else:
            print('Menos...')

    # A cada iteração do while loop o total de jogadas recebe ela mesma mais 1
    total_jogadas += 1

# No final damos um print falando que o jogador ganhou e o seu total de jogadas.
print('O computador jogou {} e você jogou {}, portanto você acertou!'.format(computador, jogador))
print('E o seu total de jogadas foi {}'.format(total_jogadas))
