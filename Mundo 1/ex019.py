'''Sortear um nome dos 4 e mostrar'''
import random
n1 = input('Informe o nome de 1 aluno: ')
n2 = input('Informe o nome de mais 1 aluno: ')
n3 = input('Informe o nome de mais 1 aluno: ')
n4 = input('Informe o nome de mais 1 aluno: ')
lista = [n1,n2,n3,n4]
sorteado = random.choice(lista)
print(f'O nome sorteado para apagar o quadro foi: {sorteado}')





