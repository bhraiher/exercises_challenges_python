'''Faça um algorítimo que leia o salário de um funcionário e mostre seu novo salário
com 15% de aumento.'''
sal = float(input('Informe qual é o salário do funcionário: R$ '))
salReajust = sal + (sal*15/100)
print('Um funcionário que ganhava R$ {}, com o reajuste de 15%, passou a ganhar R$ {:.2f}'.format(sal,salReajust))