#importar randint
from random import randint

#importar módulo sleep, que serve para "atrasar" o tempo de execução do código
from time import sleep

items = ('Rock','Paper','Scissor')

computer = randint(0,2)

#opções de jogo
print('Your game options are: [0] ROCK, [1] PAPER, [2] SCISSOR')
print('---'*12)

#vez do jogador escolher
player = int(input('What is your move? :  '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(2)
print('---'*12)

#mostrar as jogadas
print(f'Computer chose: {items[computer]}')
print(f'The player chose: {items[player]}')
print('---'*12)

#condicionais
if computer == 0:
    if player == 0:
        print('Is a draw!')
    elif player == 1:
        print('Player won!')
    elif player == 2:
        print('Computer wins!')
    else:
        print('Invalid move!')

if computer == 1:
    if player == 1:
        print('Is a draw')
    elif player == 0:
        print('Computer wins!')
    elif player == 2:
        print('Player wins!')
    else:
        print('Invalid move!')

if computer == 2:
    if player == 2:
        print('Is a draw!')
    elif player == 0:
        print('Player wins!')
    elif player == 1:
        print('Computer wins!')
    else:
        print('Invalid move!')