'''Faça um programa que verifique o nome de uma cidade diitada e diga se ela começa ou não com o nome SANTO'''
cidade = input('Inorme o nome da cidade: ')

cid_up = cidade.upper()
cid_nome = cid_up.split()
print(cid_nome[0] == 'SANTO')