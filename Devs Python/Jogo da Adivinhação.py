from random import randint
from time import sleep

#Faz o computador pensar em um número.
comp = randint(0, 10) 

print('-=-' *20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' *20)

#Jogador tenta adivinhar.
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == comp:
    print('Parabéns, você conseguiu me vencer!')    
else:
    print('GANHEI! Eu pensei no número {} e não no {}!' .format(comp, jogador))
