'''Faça um programa que leia o comprimento do cateto oposto e o cateto admjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa'''
import math
co = float(input('Informe o cateto oposto: '))
ca = float(input('informe o cateto adjacente: '))
print('A hipotenusa é: {:.2f}'.format(math.hypot(co,ca)))
#ou
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa é: {:.2f}'.format(hi))