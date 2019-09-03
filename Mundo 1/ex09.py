#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
n1 = int(input('Informe qual é a tabuada desejada: '))
lista = []
x=1
print('-'*20)
while x <= 10:
    resultado = x * n1
    print('{} X {:2}  = {}'.format(n1,x,resultado))
    x= x+1


print('-'*20)