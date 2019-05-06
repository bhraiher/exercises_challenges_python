'''Crie um programa que leia um nmr real qualquer pelo teclado e mostree na tela a sua proporção inteira'''
from math import trunc
nmr = float(input('Digite um número com ponto fluente: '))
div = nmr/5
print('A parte inteira deste numero é: {}'.format(trunc(div)))
print ('A porção inteira do resultado da divisão é {:.0f}'.format(div))
print('A porção inteira do resultado da divisão é: {}'.format(int(div)))