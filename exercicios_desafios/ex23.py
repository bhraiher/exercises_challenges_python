'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados. EX:
Digite um número: 1834
Dezena: Unidade: 4 Dezena: 3 Centena: 8 Milhar: 1'''
from tqdm import tqdm

opcao = int(input('Escolha a opção 1 para número menores de milhar, e 2 para numeros com milhar: '))
while opcao < 1 or opcao > 2:
    opcao = int(input('Escolha a opção 1 para número menores de milhar, e 2 para numeros com milhar: '))


try:
    if opcao == 1:
        #Modo um
        numero = int(input('Informe um número de 0 à 9999: '))
        print('Analisando o numero {}'.format(numero))
        #Verificação das unidades dos números através de divisão inteira e resto da divisão. (// é o numero inteiro da divisão e % é o resto da divisão).
        u = numero // 1 % 10
        d = numero // 10 % 10
        c = numero // 100 % 10
        m = numero // 1000 % 10

        print('\nUnidade: {}'.format(u), end='')
        print(' Dezena: {}'.format(d), end='')
        print(' Centena: {}'.format(c), end='')
        print( ' Milhar: {}'.format(m), end='.')
    elif opcao == 2:
        # Modo dois
        numero = str(input('Informe um número de 0 à 9999: '))
        print('Analisando o numero {}'.format(numero))

        print('\nUnidade: {}'.format(numero[-1]), end='')
        print(' Dezena: {}'.format(numero[-2]), end='')
        print(' Centena: {}'.format(numero[-3]), end='')
        print(' Milhar: {}'.format(numero[-4]), end='.')
except:
    print('\nVocê não informou a opção entre 1 e 2 ou digitou um numero maior do que 4 digitos (Foi requerido somente de 0 à 9999)')










