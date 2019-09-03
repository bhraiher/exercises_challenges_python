'''Fazer um que sorteie a apresentação de trabalhos dos alunos. O programa deve ler o nome de quatro alunos e mostrar a ordem de apresentação.'''
import random
al1 = input('Informe o primeiro aluno: ')
al2 = input('Informe o segundo aluno: ')
al3 = input('Informe o terceiro aluno: ')
al4 = input('Informe o quarto aluno: ')

alunos = [al1,al2,al3,al4]
random.shuffle(alunos)

for i,x in enumerate(alunos):
    i = i + 1
    print('A ordem ficou para apagar o quadro ficou: {}- {}'.format(i,x))