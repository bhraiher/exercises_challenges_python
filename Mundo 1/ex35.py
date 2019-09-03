'''Desenvolva um prorama que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um trângulo.'''
print('='*40)
print('Analisador de triângulos')
print('='*40)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo  segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com os segmentos informados, É POSSÍVEL formar um triângulo!')
else:
    print('Os segmento à cima NÃO PODEM formar um triângulo!')
