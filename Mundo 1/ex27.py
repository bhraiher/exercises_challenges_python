'''O seu programa deve ser capaz de ler o nome completo de uma pessoa, e informar qual é o primeiro e qual é o ultimo nome'''
n = input('Informe seu nome completo: ')
nome = n.split()
print('Olá {}, seja bem vindo(a)!'.format(n.strip()))
print('O seu primeiro nome é: {}'.format(nome[0].strip()))
print('E o seu ultimo nome é: {}'.format(nome[-1].strip()))
