'''Aula 12 - Condições aninhadas'''
#exemplo1:
nome = str(input('Qual é seu nome: '))
if nome == 'Bruno':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Paulo' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é normal.')

print('Tnha um bom dia {}'.format(nome))