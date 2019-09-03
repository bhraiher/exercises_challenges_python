'''Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto'''
print('       .:Bem-vindo à sua calculadora de descontos:.')
preco = float(input('Informe o preço: R$'))
vlrDesc = preco * 0.05
vlrDesc = preco - vlrDesc
print(f'O valor é: {vlrDesc}')
