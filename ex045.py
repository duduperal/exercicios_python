from random import choice
from time import sleep
# O computador escolhe uma jogada
lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(lista)

# Pegamos a jogada do jogador
print('''
DIGITE 
Pedra  | Papel  | Tesoura''')
print('-=' * 20)
jogador = str(input('Escolha sua jogada: '))
jogador = jogador.upper().strip()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 20)
print('Computador jogou {}\nJogador jogou {}'.format(computador.capitalize(), jogador.capitalize()))
print('-=' * 20)

# JEITO GUANABARA
if computador == 'PEDRA':
    if jogador == 'PAPEL':
        print('JOGADOR VENCE')
    elif jogador == 'TESOURA':
        print('COMPUTADOR VENCE')
    elif jogador == 'PEDRA':
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 'PAPEL':
    if jogador == 'PEDRA':
        print('COMPUTADOR VENCE')
    elif jogador == 'TESOURA':
        print('JOGADOR VENCE')
    elif jogador == 'PAPEL':
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 'TESOURA':
    if jogador == 'PEDRA':
        print('JOGADOR VENCE')
    elif jogador == 'PAPEL':
        print('COMPUTADOR VENCE')
    elif jogador == 'TESOURA':
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')

# MEU JEITO
# Checa todas as jogadas
#if jogador == computador:
    #print('EMPATE!')
#elif jogador == 'PEDRA' and computador == 'PAPEL':
    #print('COMPUTADOR VENCE')
#elif jogador == 'PEDRA' and computador == 'TESOURA':
    #print('JOGADOR VENCE')
#elif jogador == 'PAPEL' and computador == 'TESOURA':
    #print('COMPUTADOR VENCE')
#elif jogador == 'PAPEL' and computador == 'PEDRA':
    #print('JOGADOR VENCE')
#elif jogador == 'TESOURA' and computador == 'PEDRA':
    #print('COMPUTADOR VENCE')
#elif jogador == 'TESOURA' and computador == 'PAPEL':
    #print('JOGADOR VENCE')
