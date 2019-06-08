'''Escrever um programa que leia um nome e mostre o seguinte:
A: Informe o nome inteiro com letras maiusculas
B: Com letra minusculas
C: Quantidade de letras tem o nome sem espaço
D: O Primeiro nome e a qantidade de letras'''

'''Recebe o nome da pessoa'''
nome_pessoa = str(input('Informe seu nome completo: '))
nome_pessoa_maiusculo = nome_pessoa.upper()
nome_pessoa_minusculo = nome_pessoa.lower()
nome_pessoa_quebra = nome_pessoa.strip()
nome_tamanho = len(nome_pessoa_quebra) - nome_pessoa_quebra.count(' ')
nome_quebra_split = nome_pessoa.split()

print('split {}'.format(nome_pessoa_quebra))

print('O Nome em maiusculo é: {}'.format(nome_pessoa_maiusculo))
print('O Nome em minusculo é: {}'.format(nome_pessoa_minusculo))
print('O nome tem um total de {} letras'.format(nome_tamanho))
print('O primeiro nome é {} e tem {} letras'.format(nome_quebra_split[0],len(nome_quebra_split[0])))


