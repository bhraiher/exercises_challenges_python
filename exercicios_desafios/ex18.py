'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente deste ângulo.'''
import math
g = float(input('Informe o angulo: '))
rg = math.radians(g)
seno = math.sin(rg)
cos = math.cos(rg)
tang = math.tan(rg)
print('O seno de {} é {:.2f}'.format(g,seno))
print('O cosseno de {} é {:.2f}'.format(g, cos))
print('O tangente de {} é {:.2f}'.format(g, tang))