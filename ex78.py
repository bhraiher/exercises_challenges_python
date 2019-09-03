'''Fazer um programa que leia 5 valores e guardem em uma lista; No final mostrar o maior e o menor valor e suas respectivas posições na lista.'''
valores = []
for x in range(5):
    vlr_dig = int(input(f'informe o valor para posição {x}: '))
    valores.append(vlr_dig)
print('=-'*30)
print('O valor máximo foi {}' .format(max(valores)))
print('O valor minimo foi {}' .format(min(valores)))
for c, v in enumerate(valores):
    if v == max(valores):
        print(f'O maior valor se encontra na posição {c}')
    elif v == min(valores):
        print(f'O menor valor se encotnra na posicao {c}')

print('Fim do programa!')


