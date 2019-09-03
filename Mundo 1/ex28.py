'''Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
import random
from time import sleep
numero_pc = random.randint(0,5) #Faz o pc pensar.
numero_human = int(input('Advinhe o número gerado pelo computador de 0 a 5: '))

print('Processando!!')
sleep(3)
#Condição para verificar se o usuario digitou o mesmo numero gerado pelo random.
if numero_pc == numero_human:
    print('Você venceu!')
else:
    print('Voce perdeu!')

print('O número informado pelo computador foi {}'.format(numero_pc))